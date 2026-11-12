# 2. 面向对象深挖

本章讨论 Java 面向对象的几块基础：访问控制、继承与组合、抽象类与接口、多态、`equals`/`hashCode`、`record`、`static`，以及重写与重载的区别。

对应代码：[`OopDemo.java`](./src/main/java/com/jffd/core/oop/OopDemo.java)（同包还有 `Payment`、`CheckoutService`、`User`、`UserId` 等）

| | |
|--|--|
| 前置 | 第 1 章：基本类型与引用类型、`==` 与 `equals`。 |
| 学完应能 | 用 `private` 封装字段；用接口 + 组合表达策略；区分抽象类与接口；正确重写 `equals`/`hashCode`；说明 `record` 适合什么。 |

下面从「一个类如何隐藏内部状态」开始，按顺序读，不要跳。

---

## 2.1 封装与访问修饰符

**封装**的意思是：把对象的内部数据藏起来，只通过受控的方法对外交互。

Java 用访问修饰符限制「谁能看见这个成员」：

| 修饰符 | 同类 | 同包 | 子类 | 其他包 |
|--------|------|------|------|--------|
| `private` | 可以 | 不可以 | 不可以 | 不可以 |
| 默认（不写修饰符，包私有） | 可以 | 可以 | 不可以* | 不可以 |
| `protected` | 可以 | 可以 | 可以 | 不可以 |
| `public` | 可以 | 可以 | 可以 | 可以 |

\*子类若在别的包，也看不到父类的包私有成员。

常见写法：

```java
public class User {
    private final long id;
    private String email;

    public User(long id, String email) {
        this.id = id;
        this.email = email;
    }

    public long getId() { return id; }
    public String getEmail() { return email; }
}
```

建议：

- 字段默认 `private`，不要写成 `public int age`。  
- 对外提供方法；不要无脑给每个字段生成 setter——有些状态改了会破坏不变量（例如已支付订单的金额）。  
- 包私有适合「同模块内部协作」。

---

## 2.2 继承、组合与接口实现

Java 表达「类型之间关系」主要有三种方式，先分开记：

1. **`extends`（继承）** — A **是一种** B（is-a）。一个类只能继承一个父类。  
2. **成员字段（组合）** — A **拥有** 一个 B（has-a）。  
3. **`implements`（实现接口）** — A **具备** 某种能力（can-do）。一个类可以实现多个接口。

![继承、组合与接口](./assets/composition-vs-inheritance.svg)

先看组合的例子——结账服务**拥有**一个支付能力，而不是继承支付：
```java
final class CheckoutService {
    private final Payment payment;

    CheckoutService(Payment payment) {
        this.payment = payment;
    }

    void checkout(int cents) {
        payment.pay(cents);
    }
}
```

再看接口：

```java
public interface Payment {
    void pay(int cents);
}

public class AlipayPayment implements Payment {
    @Override
    public void pay(int cents) { /* ... */ }
}
```

日常选型：

- 真正的 is-a、且树很浅时，才考虑 `extends`。  
- 复用行为优先「接口 + 组合」。  
- 深继承容易出现**脆弱基类**问题：父类改一个 `protected` 方法，子类行为可能静默变化。

到了 Spring，构造器注入就是组合：`OrderService(OrderRepository repo, PaymentGateway gw)`。本章是后面 IoC 的预科。

---

## 2.3 抽象类与接口

**接口**声明一组方法契约，类通过 `implements` 承诺实现它们。  
**抽象类**可以既有抽象方法，也有已实现的方法和字段；不能直接 `new`，只能被继承。

```java
public abstract class AbstractNotifier {
    public final void notifyUser(String to, String body) {
        validate(to);
        String text = format(body);
        doSend(to, text);
        afterSend(to);
    }

    protected void validate(String to) { /* 默认校验 */ }
    protected String format(String body) { return body; }
    protected abstract void doSend(String to, String text);
    protected void afterSend(String to) { /* 可选钩子 */ }
}
```

上面是**模板方法**：流程固定在 `notifyUser`，子类只填必须实现的步骤。

| 需求 | 更倾向抽象类 | 更倾向接口 |
|------|--------------|------------|
| 需要共享字段或受保护状态 | 是 | 否 |
| 需要同时具备多种能力 | 否（单继承） | 是（可多实现） |
| 固定算法骨架、子类填洞 | 是 | 较少 |
| 对外 API、策略点、SPI | 较少 | 是 |

Java 8 之后接口可以有 `default` / `static` 方法，但接口仍不宜当成「带一堆状态的基类」来用。

---

## 2.4 多态

**多态**在这里指：用父类型（或接口类型）的变量，指向子类型（或实现类）的对象；编译期按左边类型检查能调哪些方法，运行期按右边实际对象执行哪段实现。

![多态：按实际对象类型分发](./assets/polymorphism-dispatch.svg)

```java
Payment pay = new AlipayPayment();
pay.pay(100); // 编译期看 Payment；运行期进入 AlipayPayment
```

业务代码只依赖 `Payment`，换支付渠道时替换实现即可。这是策略模式、插件化，以及 Spring 注入 `List<Handler>` 的基础。

---

## 2.5 `equals`、`hashCode` 与 `toString`

第 1 章说过：`==` 对引用比对的是「是不是同一个对象」；内容是否相等通常靠 **`equals`**。

放入 `HashMap` / `HashSet` 时，还要遵守额外契约：

1. `equals` 应自反、对称、传递、一致；与 `null` 比较返回 `false`。  
2. 若 `equals` 为 `true`，则 `hashCode` **必须**相等。  
3. `hashCode` 相等不一定 `equals`（哈希冲突正常）。  
4. 参与 `equals`/`hashCode` 的字段，在对象进入集合之后不要再改（可变 key 问题见第 3 章）。

```java
@Override
public boolean equals(Object o) {
    if (this == o) return true;
    if (!(o instanceof User user)) return false;
    return Objects.equals(id, user.id);
}

@Override
public int hashCode() {
    return Objects.hash(id);
}
```

只重写 `equals`、不重写 `hashCode`，集合行为会错乱。`toString` 建议重写成对调试有用的内容。

### `record`（Java 16+）

**`record`** 是一种专门表示「不可变数据载体」的类声明。编译器会生成构造器、访问器、`equals`、`hashCode`、`toString`。

```java
public record UserId(long value) {
    public UserId {
        if (value <= 0) throw new IllegalArgumentException("must be positive");
    }
}
```

适合：标识符、值对象、简单不可变 DTO。  
不太适合：需要复杂继承或可变生命周期的实体（持久化实体后面再讲）。

---

## 2.6 `static`

`static` 成员属于**类本身**，不属于某个实例。所有实例共享同一份 static 字段。

```java
public class Cache {
    private static Map<String, Object> DATA = new HashMap<>(); // 进程内共享，可变时很危险
}
```

建议：

- 常量可以用 `public static final`。  
- 不要随手把可变 Map 放成 static「全局缓存」。  
- 「全进程一份的服务」交给容器管理的单例（后面 Spring），不要急着手写各种 `getInstance()`。

多线程下 static 可变状态的问题，模块二再展开。

---

## 2.7 重写与重载

| | 重载 overload | 重写 override |
|--|---------------|---------------|
| 发生位置 | 同一类中（或子类新增同名不同参方法） | 子类对父类 / 接口 |
| 签名 | 方法名相同，参数列表不同 | 方法名与参数类型序列相同 |
| 目的 | 同一语义、不同入参 | 替换或特化父类行为 |

子类重写父类方法时加上 `@Override`：写错签名时编译器会报错，而不是悄悄变成新的重载。

---

## 检验一下

1. 字段为什么默认写成 `private`？  
2. 组合和继承各适合什么关系？  
3. 抽象类和接口如何选择？  
4. 为什么重写 `equals` 必须重写 `hashCode`？  
5. `record` 自动生成了哪些东西？适合什么场景？

---

## 动手

1. 运行：

```bash
mvn -pl 01-Java-Core-And-OOP exec:java -Dexec.mainClass="com.jffd.core.oop.OopDemo"
```

2. 观察同一 `Payment` 类型、不同实现走不同渠道。  
3. 对照模板方法：`notifyUser` 流程固定，子类只填发送。  
4. 确认替换支付实现不必改 `CheckoutService`。  
5. 确认同 id 的两个 `User` 进 `HashSet` 后 size 为 1；再看 `UserId` record。

---

## 避坑

1. 深继承，并随意覆写父类契约  
2. 实体 `equals` 只比 id，临时对象 id 为 null 时可能「全体相等」  
3. 可变字段参与 `hashCode`，放进 Set/Map 后再修改  
4. 接口变成「上帝接口」（方法过多、default 堆叠）  
5. static 可变 Map 当缓存

## 面试（可选）

- 抽象类和接口？Java 8 的 default/static 方法之后呢？  
- 重写 `equals` 为什么必须重写 `hashCode`？  
- 组合优于继承的常见理由？  
- 多态如何分派（了解虚方法表即可）？  
- 深拷贝与浅拷贝？为什么不太推荐 `Object.clone`？

## 小结

本章把「类如何协作」立住了：封装隐藏状态，接口声明能力，组合组装行为，多态按实际对象分派；放进集合前必须同时想清楚 `equals` 与 `hashCode`。下一章专门讲集合本身。

下一章 → [03-collections-framework.md](./03-collections-framework.md)
