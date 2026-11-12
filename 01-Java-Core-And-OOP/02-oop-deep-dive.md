# 2. 面向对象深挖

> 先搞清三件事：名义类型、组合优于继承、`equals` 契约。然后再看 Demo。  
> 对应：[`OopDemo.java`](./src/main/java/com/jffd/core/oop/OopDemo.java)（同包还有 `Payment`、`CheckoutService`、`User`、`UserId` 等）

---

## 和 TS OOP 最容易踩的三道坎

TS 更偏结构化：

```ts
type Payable = { pay(amount: number): void }
function checkout(p: Payable) { p.pay(100) }
// 长得像就能过 —— 鸭子类型
```

Java 是名义类型：

```java
void checkout(Payment p) { p.pay(100); }
// 必须显式 implements Payment，光「方法长得像」不够
```

另外两点：

1. 字段要自己封装，不能像 plain object 随手加属性。  
2. 单继承 + 多接口：复用能力优先「组合 + 接口」，别堆 `extends`。

---

## 2.1 封装：访问修饰符

| 修饰符 | 类内 | 同包 | 子类 | 全局 | 前端直觉 |
|--------|------|------|------|------|----------|
| `private` | ✅ | ❌ | ❌ | ❌ | `#field` / 闭包 |
| 默认（包私有） | ✅ | ✅ | ❌* | ❌ | monorepo 未 export |
| `protected` | ✅ | ✅ | ✅ | ❌ | 留给继承扩展 |
| `public` | ✅ | ✅ | ✅ | ✅ | `export` |

\*子类在别的包时，看不到父类的包私有成员。

怎么选：

- 字段默认 `private`，别 `public int age`。  
- 对外给方法（或 Lombok `@Getter`），别裸字段。  
- Setter 别无脑全生成。领域对象乱 set 会破坏不变量（已支付订单别再改金额）。  
- 包私有适合同模块内部协作，当成「没 export 的内部模块」。

把 class 当成「带私有状态的服务对象」，别当成可摊开的 JSON。

---

## 2.2 继承 vs 组合

```text
前端：别为了复用 UI，HOC / 基类组件叠五层
Java：别为了复用字段，Animal → Dog → Husky → ...
```

| 关系 | 关键字 | 含义 | 典型用法 |
|------|--------|------|----------|
| is-a | `extends` | 真是一种 | 谨慎，树要浅 |
| has-a | 成员字段 | 拥有某种能力 | 企业默认 |
| can-do | `implements` | 具备某种能力 | 策略、插件、SPI |

```java
// 组合：Checkout 拥有 Payment，不是继承 Payment
final class CheckoutService {
    private final Payment payment;
    CheckoutService(Payment payment) { this.payment = payment; }
    void checkout(int cents) { payment.pay(cents); }
}
```

到了 Spring，构造器注入就是这种组合：`OrderService(OrderRepository repo, PaymentGateway gw)`。  
你现在学的不是学术 OOP，是后面 IoC 的预科。

### 脆弱基类

父类改一个 `protected` 方法，子类行为可能静默变掉——跟深继承组件改 lifecycle 一个味。  
优先接口 + 组合；继承留给稳定的模板骨架，或真正的 is-a。

---

## 2.3 抽象类 vs 接口

| 你的需求 | 更该用抽象类 | 更该用接口 |
|----------|--------------|------------|
| 要存字段、共享状态 | ✅ | ❌（别拿接口当状态容器） |
| 想要多「父能力」 | ❌ 只能单继承 | ✅ 可多实现 |
| 骨架算法（模板方法） | ✅ | default 方法勉强 |
| 对外 API / SPI / 策略点 | 少用 | ✅ |
| JDK8+ 默认方法做逆向兼容 | 可以 | ✅ |

对照：

- 抽象类 ≈ 带半套实现的基类组件（规定流程，子类填洞）  
- 接口 ≈ 必须满足的 Protocol  

模板方法（本模块 `AbstractNotifier`）：

```text
notifyUser()          ← final，流程锁死
  ├─ validate()
  ├─ format()
  ├─ doSend()         ← 抽象，子类实现
  └─ afterSend()      ← 钩子，可选覆盖
```

跟「基类规定生命周期，子类实现 render」是同一套路。

---

## 2.4 多态：编译看左边，运行看右边

```java
Payment pay = new AlipayPayment();
pay.pay(100); // 编译期按 Payment 检查；运行期进 AlipayPayment
```

1. 变量类型决定你能调哪些方法。  
2. 实际对象类型决定跑哪段实现。  

这是策略模式、插件化、Spring 注入 `List<Handler>` 的基础：业务只依赖 `Payment`，换渠道 = 换注入实现。  
前端也一样：依赖 `PaymentClient` 接口，测试注入 mock，生产注入真实 SDK。

---

## 2.5 `equals` / `hashCode` / `toString`

JS 里对象进 `Set`/`Map` 默认按引用。  
Java 的 `HashMap`/`HashSet` 按 `hashCode` + `equals` 判是不是同一个键。  
只重写 `equals` 不重写 `hashCode`，集合行为会像闹鬼。

契约：

1. `equals`：自反、对称、传递、一致；对 `null` 返回 false。  
2. `equals` 为 true ⇒ `hashCode` 必须相等。  
3. `hashCode` 相等不一定 `equals`（冲突正常）。  
4. 参与比较的字段，进集合后别再改（可变 key 见第 3 章）。

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

### `record`（Java 16+）

```java
public record UserId(long value) {
    public UserId {
        if (value <= 0) throw new IllegalArgumentException("must be positive");
    }
}
```

自动生成构造器、访问器、`equals`、`hashCode`、`toString`。  
直觉上像 `Readonly<{ value: number }>` + 结构化相等，还带校验。

适合：标识符、金额值对象、不可变 DTO 片段。  
不太适合：还要继承、复杂可变生命周期的实体（JPA 实体后面另说）。

---

## 2.6 `static`

```java
public class Cache {
    private static Map<String, Object> DATA = new HashMap<>(); // 危险：全局可变
}
```

像 ES module 顶层 `let store = {}`——热更新前一直在；SSR / 多请求共享会串数据。  
Java Web 更狠：多线程同时摸 static 可变状态（模块二展开）。

- 常量：`public static final` OK。  
- 「全进程一份的服务」交给 Spring 单例 Bean，别手写 `getInstance()` 耍帅。  
- 请求级上下文后面会碰到 `ThreadLocal`（也有泄漏坑）。

---

## 2.7 重写 vs 重载

| | 重载 Overload | 重写 Override |
|--|---------------|---------------|
| 范围 | 同类（或子类新方法） | 子类对父类 |
| 签名 | 方法名同，参数不同 | 方法名 + 参数类型序列相同 |
| 目的 | 同一语义不同入参 | 改父类行为 |

养成加 `@Override` 的习惯，写错时编译器会救你。

---

## 2.8 先自测

1. 为啥「方法长得像」也不能当接口实现？  
2. 什么时候用抽象类，什么时候用接口？  
3. 为啥重写 `equals` 必须重写 `hashCode`？  
4. 组合相比继承，在 Spring 里意味着什么？  
5. `record` 解决了什么麻烦？

---

## 2.9 动手

```bash
mvn -pl 01-Java-Core-And-OOP exec:java -Dexec.mainClass="com.jffd.core.oop.OopDemo"
```

对照：

1. 多态：同一 `Payment`，不同实现不同渠道  
2. 模板方法：`notifyUser` 流程固定，SMS 只填发送与审计  
3. 组合：换支付实现不必改 `CheckoutService`  
4. 同 id 不同 email 的 `User` → HashSet size 仍为 1  
5. `UserId` record 的 equals  

---

## 避坑

1. 深继承 + 乱覆写父类契约  
2. 实体 `equals` 只比 id，临时对象 id=null 时「全体相等」  
3. 可变字段参与 `hashCode`，放进 Set/Map 后再改  
4. 接口变成上帝接口（一堆 default）  
5. static 可变 Map 当缓存  

## 面试

- 抽象类和接口？Java 8 default/static 之后呢？  
- 重写 equals 为何必须重写 hashCode？  
- 组合优于继承的理由？  
- 多态大概怎么分派（虚方法表，了解即可）？  
- 深拷贝浅拷贝？为啥不太推荐 `clone`？

下一章 → [03-collections-framework.md](./03-collections-framework.md)
