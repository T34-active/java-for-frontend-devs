# 1. 强类型与基础语法

> 这章先把「Java 为什么这么拧」讲清楚。示例代码最后再跑。  
> 还没装好 JDK 17？先回 [00 · 安装 JDK 与工具链](./00-install-jdk-and-toolchain.md)。  
> 对应：[`StrongTypingDemo.java`](./src/main/java/com/jffd/core/typing/StrongTypingDemo.java)

---

## 你以为你会的「类型」，其实还差一层

TS 里你大概这样写：

```ts
let n: number = 1
let s: string = "2"
// n + s  —— TS 会警告；要是 any / 断言糊弄过去，运行时还可能变成 "12"
```

Java 更绝：

1. 编译期几乎不给你偷渡弱类型（没有日常路径的 `1 + "2" → "12"`）。
2. 运行时也不会像 JS 那样「尽量帮你转一下」。
3. 还有一层 TS 很少逼你正视的事：**基本类型和包装类型，运行时真是两回事**。

一句话说完：

> TS 的类型多半是给人和编译器看的标签；  
> Java 的类型还决定值放哪儿、能不能为 null、`==` 到底比什么。

---

## 1.1 基本类型 vs 包装类型

### 为啥前端容易懵

TS/JS 里 `number` / `boolean` / `string`，你当值用就行，偶尔被当成对象也无感。  
Java 是两套并存，而且业务代码天天在两套之间跳：

| Java 基本类型 | 包装类型 | ≈ 你熟悉的 | 差别 |
|---------------|----------|------------|------|
| `int` | `Integer` | `number`（整数） | 包装类型可以为 null |
| `long` | `Long` | 近似 `bigint` | 字面量要写 `100L` |
| `double` | `Double` | `number` | 算钱别用，用 `BigDecimal` |
| `boolean` | `Boolean` | `boolean` | 三态：true / false / **null** |
| `char` | `Character` | 单字符 | 日常字符串用 `String` |
| — | `String` | `string` | 引用类型，有常量池 |

### 两张图

```text
int x = 42;          → 更像栈上的纯数值，没有「空」
Integer y = 42;      → 堆上的对象（可能走缓存），可以为 null
Integer z = null;
int boom = z;        → 拆箱读 null → NullPointerException
```

不精确但好记：

- `int` ≈ 你确信永远有值的 `number`
- `Integer` ≈ `number | null`，从 null 硬转回 `number` 时直接炸，没有 `NaN` 这种缓冲

### 自动装箱 / 拆箱

编译器会帮你包一层、拆一层：

```java
Integer boxed = 42;   // Integer.valueOf(42)
int raw = boxed;      // boxed.intValue()
```

方便，也是 NPE 重灾区：你以为在算 `int`，中间其实躺着一个 null 的 `Integer`。

### Integer 缓存（面试爱问，生产别依赖）

JVM 默认缓存 **-128 ~ 127** 的 `Integer`：

```java
Integer a = 127;
Integer b = 127;
a == b;   // 常常 true（同一缓存对象）

Integer c = 128;
Integer d = 128;
c == d;   // false
c.equals(d); // true
```

包装类型比相等，用 `equals`，或先拆成基本类型。别写 `if (userId == 100L)` 去比 `Long`——小数字碰巧绿、大数字随机挂。

### 字段到底选哪个

| 场景 | 推荐 | 原因 |
|------|------|------|
| 实体 / DTO / 接口入参出参 | `Long` `Integer` `Boolean` | JSON / DB / 表单经常是「没传 = null」 |
| 局部循环、下标、累加 | `int` `long` | 少装箱 |
| 金额、汇率、费率 | `BigDecimal` | `0.1 + 0.2` 在后端会变成对账事故 |
| 开关 | 慎用 `Boolean` | `null` 进 `if (flag)` 直接 NPE |

```java
// 金额用字符串构造，别让 double 先脏了再转
BigDecimal price = new BigDecimal("10.005");
BigDecimal paid = price.setScale(2, RoundingMode.HALF_UP); // 10.01
```

前端用 `number` 算钱其实也有同样坑，后端只是更不允许你侥幸。

---

## 1.2 `==` vs `equals`

先把「JS 的 ===」拆掉重建：

| 你想表达 | JS/TS | Java |
|----------|-------|------|
| 是不是同一个引用 | 对象用 `===` | `==` |
| 内容是否相等 | 自己比 / 库 | `equals`（类得正确实现） |
| 两边都可能 null | 手写 | `Objects.equals(a, b)` |

```java
String a = new String("hello");
String b = new String("hello");
a == b;        // false：两个堆对象
a.equals(b);   // true：字符序列相同
```

### String 常量池：知道就行，别当特性用

```java
String c = "hello";
String d = "hello";
c == d; // 常常 true（字面量进池，复用引用）
```

业务里别靠 `==` 比字符串。今天池化帮你绿了，明天 `new String`、拼接、反序列化进来，测试就红。

对照前端：

```ts
const a = { id: 1 }
const b = { id: 1 }
a === b  // false：引用
// 内容相等得自己写，或 lodash isEqual
```

Java 没有默认的「结构相等」魔法：`==` 很老实，`equals` 看类作者有没有尽责。

---

## 1.3 `final` ≈ `const`，只锁引用

```java
final List<String> list = new ArrayList<>();
list.add("ok");              // 内容可变
// list = new ArrayList<>(); // 引用不能换
```

跟前端一样：

```ts
const list = ["a"]
list.push("b")     // 可以
// list = []       // 不行
```

所以 `final` ≠ 深不可变。深不可变靠 `List.of` / `Map.of`、`record`、或防御性拷贝：

```java
List<String> freeze = List.of("x", "y");
// freeze.add("z"); // UnsupportedOperationException
```

参数、局部变量能 `final` 就 `final`，后面讲并发会受益。

---

## 1.4 数组 vs 集合：业务默认选集合

```java
String[] arr = {"a", "b"};     // 定长
List<String> list = new ArrayList<>();
list.add("c");                 // 变长，API 多
```

| | 数组 `T[]` | `List` 等集合 |
|--|-----------|---------------|
| 长度 | 创建时固定 | 可变 |
| 泛型 | 有坑（协变） | 一等公民 |
| API | 贫瘠 | `add/remove/stream/...` |
| 业务使用率 | 低 | 高 |

`T[]` 像定长 TypedArray；日常业务直接脑补成 `ArrayList`。原始数组多见于 JNI、性能热点、`main(String[] args)`。  
集合整章见第 3 章；这里先立偏好：**新代码优先 `List`/`Map`/`Set`**。

---

## 1.5 方法、重载、`var`

### 重载是真的

```java
void print(String s) { }
void print(int n) { }   // 同名，参数列表不同
```

TS 也有重载声明，常常是一套实现 + 多个签名。Java 是编译期按参数类型分到不同方法。别和「重写 Override」混——重写是父子同签名，下一章。

### `var`（Java 10+）

```java
var name = "Ada";     // 推断为 String
// var x = null;      // 推不出来
```

右边一眼能看出类型时用 `var` 挺好；复杂泛型嵌套还是写全，读的人谢谢你。公开 API 的返回类型别玩推断思维，签名写清楚。

---

## 1.6 空安全：NPE 与 Optional

TS 有：

```ts
user?.profile?.city
```

Java 17 日常没有同等普及的语言级可选链（注解、第三方另说），这些都会炸：

```java
Integer x = null;
int y = x;                    // 拆箱 NPE

user.getProfile().getCity();  // 中间 null

map.get("k").toString();      // get 到 null

Boolean flag = null;
if (flag) { }                 // 拆箱 NPE
```

### Optional：用途要对

`Optional<T>` 的意思是：这个返回值可能没有，调用方请显式处理。

```java
Optional<String> opt = Optional.ofNullable(findName());
String show = opt.orElse("anonymous");
opt.ifPresent(name -> System.out.println(name));
String must = opt.orElseThrow(() -> new IllegalStateException("missing"));
```

常见约定：

| 做 | 别做 |
|------|------|
| 用在返回值表达「可能空」 | 当实体字段类型到处飞 |
| `orElse` / `orElseThrow` / `map` | 无脑 `get()` |
| 集合没数据返回 `List.of()` | 返回 `null` 列表 |
| 入参 `Objects.requireNonNull(x, "x")` | 假设别人永不传 null |

常量在前的 equals：

```java
"admin".equals(role);  // role 为 null → false，不炸
role.equals("admin");  // role 为 null → NPE
```

---

## 1.7 String 补一刀

- `String` 不可变：看起来像改，常常是新对象；循环拼接用 `StringBuilder`。
- 业务比内容用 `equals` / `Objects.equals`。
- `isBlank()`（Java 11+）比只判 `null` / `isEmpty()` 更贴近表单。
- 别无故 `new String("x")`。

```java
String full = first + "-" + second;           // 少量 OK
StringBuilder sb = new StringBuilder();
for (String p : parts) sb.append(p).append(',');
```

---

## 1.8 先别看代码，自己答一遍

1. 实体里的 id 为啥常用 `Long` 而不是 `long`？
2. `Integer a = 128; Integer b = 128; a == b` 多半怎样？该怎么比？
3. `final` 能保证 List 内容不变吗？
4. `Optional` 适合当数据库实体字段吗？
5. 金额为啥不能 `double`？

答得上来再去看 / 跑 `StrongTypingDemo`。

---

## 1.9 动手

```bash
mvn -pl 01-Java-Core-And-OOP exec:java -Dexec.mainClass="com.jffd.core.typing.StrongTypingDemo"
```

建议对照顺序：

1. Integer 缓存内外的 `==`
2. `new String` 与字面量的 `==` / `equals`
3. `0.1 + 0.2` 的 double 与 BigDecimal
4. 取消注释拆箱 NPE 那行，读堆栈第一帧

---

## 避坑

1. `Boolean` / `Integer` 拆箱进 `if` 或运算 → NPE  
2. 包装类型用 `==` → 间歇性假绿  
3. 金额用 `double`  
4. 字符串用 `==`  
5. 接口返回 `null` List（应返回空集合）  
6. `Optional` 当字段，或无脑 `get()`  

## 面试（能口头说清就行）

- 基本类型和包装类型？装箱拆箱？拆箱为啥 NPE？  
- `Integer` 缓存范围？为啥不能 `==`？  
- `==` 和 `equals`？`String` 为啥有时 `==` 为 true？  
- `final` 修饰变量 / 方法 / 类？  
- `String` 为啥不可变？  
- `Optional` 适用场景和反模式？

下一章 → [02-oop-deep-dive.md](./02-oop-deep-dive.md)
