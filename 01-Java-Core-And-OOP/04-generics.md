# 4. 泛型

> TS 泛型你已经会了。这章重点是 Java 的擦除和 PECS——卡编译器的地方多半在这。  
> 对应：[`GenericsDemo.java`](./src/main/java/com/jffd/core/generics/GenericsDemo.java)

---

## 和 TS Generics 的同与不同

相同点：

```ts
type ApiResponse<T> = { code: number; message: string; data: T }
function first<T>(arr: T[]): T | undefined { return arr[0] }
```

```java
public class ApiResponse<T> { ... }
public static <T> T first(List<T> list) { ... }
```

最大不同：

> Java 泛型主要在编译期存在，运行时会擦除。  
> TS 类型也会擦掉，但 Java 因此多了「不能 `new T()`、不能写 `List<String>.class`」这类硬限制。

---

## 4.1 为啥要泛型

远古写法：

```java
List list = new ArrayList();
list.add("x");
list.add(1);
String s = (String) list.get(1); // 运行时 ClassCastException
```

有了泛型：

```java
List<String> list = new ArrayList<>();
list.add("x");
// list.add(1); // 编译失败 —— 就是 TS 教过你的价值
```

钻石操作符 `<>`：右边可推断。

```java
Map<String, List<Integer>> map = new HashMap<>();
```

---

## 4.2 泛型类 / 方法 / 接口

```java
public class Box<T> {
    private T value;
    public void set(T value) { this.value = value; }
    public T get() { return value; }
}

public static <T> T first(List<T> list) {
    return list.isEmpty() ? null : list.get(0);
}
```

方法上的 `<T>` 写在返回类型前面，是「该方法自己的类型参数」，可以和类上的 `<T>` 不是一回事。

命名习惯：`T` 类型、`E` 元素、`K`/`V` 键值、`R` 返回值。  
后端天天见：`Result<T>`、`Page<T>`、`Repository<T, ID>`。

---

## 4.3 通配符与 PECS

Java 泛型默认不变（invariant）：

```java
List<Integer> ints = List.of(1, 2);
// List<Number> nums = ints; // 编译错误
```

数组不一样（协变，且不安全）：

```java
Number[] arr = new Integer[2];
arr[0] = 1.5; // 编译过，运行 ArrayStoreException
```

所以用通配符表达有限的协变/逆变：

| 写法 | 读作 | 能做什么 | 前端直觉 |
|------|------|----------|----------|
| `List<? extends Number>` | 某种 Number 子类型列表 | 主要能读成 Number；不能随意 add | 只读协变 |
| `List<? super Integer>` | 某种 Integer 父类型列表 | 能 add Integer；读出来当 Object | 只写逆变 |
| `List<?>` | 未知 | 几乎只能读 Object | `unknown[]` |

口诀：Producer Extends，Consumer Super。

```java
static double sum(List<? extends Number> source) {
    double total = 0;
    for (Number n : source) total += n.doubleValue();
    // source.add(1); // 不行：说不定是 List<Double>
    return total;
}

static void fill(List<? super Integer> sink) {
    sink.add(10);
    // Integer x = sink.get(0); // 不行：可能是 List<Object>
}
```

你想写「既能处理 `List<Integer>` 也能处理 `List<Double>` 的求和」——没有 `? extends` 就得复制两套。  
TS 的 `T extends Foo` 你很熟；Java 的 `? extends` / `? super` 是使用处通配，别硬套成同一套语法糖。

---

## 4.4 类型擦除

编译后大致变成「原始类型 + 必要强制转换」：

```text
List<String>  →  List
List<Integer> →  List
```

因此不能：`new T()`、`new T[10]`、`List<String>.class`、`catch (T)`、运行时 `instanceof List<String>`。

需要运行时类型时，把 `Class<T>` 当令牌传进来——类似把 zod schema / class constructor 传进工厂：

```java
public static <T> T create(Class<T> type) throws Exception {
    return type.getDeclaredConstructor().newInstance();
}
String s = create(String.class);
```

Jackson 反序列化泛型常用 `TypeReference<List<User>>`，也是在补运行时信息（模块三再碰）。

桥接方法了解即可：擦除后为保住多态，编译器可能生成合成方法。面试提到「擦除 + 桥接」够用。

---

## 4.5 边界

```java
public static <T extends Comparable<T>> T max(T a, T b) {
    return a.compareTo(b) >= 0 ? a : b;
}
```

≈ TS：`function max<T extends Comparable<T>>(a: T, b: T): T`

多界：`<T extends Animal & Serializable & Comparable<T>>`，类只能放第一个，其余是接口。

---

## 4.6 泛型与数组：别混

数组协变、运行时知分量类型 → 可能 `ArrayStoreException`。  
泛型不变、运行时擦除 → 更偏编译期安全。  

容器优先 `List<T>`。看到 `unchecked` 警告别无脑压制，先想办法消掉。

---

## 4.7 和后端现实的关系

你会不断写 `ApiResponse<UserVO>`、`Page<Order>`、各种 `List<Foo>`。擦除的实际影响：

1. 反射拿到的字段可能是擦除后的信息，框架靠额外元数据补。  
2. JSON 反序列化必须告诉框架「这是 `List<User>` 不是 `List`」。  
3. 公共 API 别返回原始类型 `List`，会污染调用方。

---

## 4.8 先自测

1. 为啥 `List<Integer>` 不能直接当 `List<Number>`？  
2. PECS 分别解决读和写哪边？  
3. 为啥不能 `new T()`？常见绕法？  
4. 数组协变和泛型不变，哪个更危险？  
5. `ApiResponse<T>` 为啥适合泛型？

---

## 4.9 动手

```bash
mvn -pl 01-Java-Core-And-OOP exec:java -Dexec.mainClass="com.jffd.core.generics.GenericsDemo"
```

对照：`Box`、`ApiResponse`、`sum(? extends)`、`fill(? super)`、`Class<T>` 工厂。

---

## 避坑

1. 原始类型 `List` 与 `List<String>` 混搭  
2. 乱 `@SuppressWarnings("unchecked")`  
3. 返回 `List<?>` 导致调用方什么都加不了  
4. 硬造泛型数组  
5. 以为运行时还能区分 `List<String>` 和 `List<Integer>`  

## 面试

- 类型擦除？有哪些限制？  
- `? extends` 与 `? super`？PECS？  
- 泛型与数组差异？  
- 如何获取泛型运行时类型信息？  
- 桥接方法是什么？（加分）

下一章 → [05-stream-and-lambda.md](./05-stream-and-lambda.md)
