# 5. Stream 与 Lambda

> 你会 `map/filter/reduce` 就已经赢在起跑线。这章补 Java Stream 的惰性、一次性、collect、并行陷阱。  
> 对应：[`StreamDemo.java`](./src/main/java/com/jffd/core/stream/StreamDemo.java)

---

## 像极了，但别当成 Array 方法集

```ts
users
  .filter(u => u.age >= 18)
  .map(u => u.name)
  .sort()
```

```java
users.stream()
    .filter(u -> u.age() >= 18)
    .map(UserView::name)
    .sorted()
    .toList();
```

三处差别：

1. Stream 用过就废，不能像数组反复 `map`。  
2. 中间操作惰性，碰到终端操作才真正算。  
3. `parallelStream()` 是真并行线程，不是 `Promise.all` 那种 IO 调度直觉。

---

## 5.1 Lambda 与函数式接口

```java
BinaryOperator<Integer> add = (a, b) -> a + b;
Runnable r = () -> System.out.println("hi");

list.forEach(System.out::println);
list.stream().map(String::toUpperCase);
list.stream().map(User::name);
```

| 接口 | 形态 | ≈ TS | 典型场景 |
|------|------|------|----------|
| `Function<T,R>` | T → R | `(t)=>R` | map |
| `Predicate<T>` | T → boolean | 断言 | filter |
| `Consumer<T>` | T → void | 副作用 | forEach |
| `Supplier<T>` | () → T | 工厂 | 懒创建 |
| `UnaryOperator<T>` | T → T | 同型映射 | |
| `BinaryOperator<T>` | (T,T)→T | reduce | |

目标类型得是只有一个抽象方法的接口（`@FunctionalInterface`）。  
跟 TS「函数当值」一样，只是必须落在某个接口类型上。

### 变量捕获

外层局部变量必须是 final 或事实上 final：

```java
int factor = 2;
list.stream().map(x -> x * factor); // OK
// factor = 3; // 再改就不让捕获了
```

前端闭包更自由；这份限制能减少「抓了个会变的变量」——并行时更明显。

---

## 5.2 对照表

| JS / lodash | Java Stream |
|-------------|-------------|
| `map` | `map` / `mapToInt`… |
| `filter` | `filter` |
| `reduce` | `reduce` / **`collect`** |
| `flatMap` | `flatMap` |
| `find` / `some` | `findFirst` / `anyMatch` |
| `every` | `allMatch` |
| `slice` | `skip` + `limit` |
| `sort` | `sorted` |
| `join` | `Collectors.joining` |
| `groupBy` | `Collectors.groupingBy` |
| `uniq` | `distinct` |

```java
List<String> result = users.stream()
    .filter(u -> u.age() >= 18)
    .map(UserView::name)
    .sorted()
    .toList(); // Java 16+；老代码 collect(Collectors.toList())
```

---

## 5.3 中间操作 vs 终端操作

```text
创建 Stream
   │  filter / map / flatMap / sorted / peek ...   ← 中间：惰性，搭管道
   ▼
终端：collect / toList / forEach / findFirst / count / reduce ...
   │
   ▼
触发计算；之后 Stream 作废
```

```java
List.of(1, 2, 3, 4, 5).stream()
    .filter(n -> {
        System.out.println("filter " + n);
        return n % 2 == 0;
    })
    .map(n -> {
        System.out.println("map " + n);
        return n * n;
    })
    .findFirst();
// 往往不会跑完 1..5：短路
```

像生成器 / 惰性迭代，不是每步都物化成新数组。  
`peek` 只建议调试用，别在生产管道里塞业务副作用。

---

## 5.4 `collect` 才是业务主力

分组、拼接、下游统计，优先 Collectors：

```java
Map<String, Long> countByDept = emps.stream()
    .collect(Collectors.groupingBy(Emp::dept, Collectors.counting()));

Map<String, Integer> salarySum = emps.stream()
    .collect(Collectors.groupingBy(Emp::dept, Collectors.summingInt(Emp::salary)));

String csv = emps.stream()
    .map(Emp::name)
    .collect(Collectors.joining(", "));
```

`groupingBy` ≈ lodash `groupBy` + 各种下游聚合。报表、列表变 Map 时天天用。

---

## 5.5 `map` vs `flatMap`

```text
map：     1 入 → 1 出（形态变，层数不变）
flatMap： 1 入 → 0..n 出，并摊平一层
```

```java
List<Optional<String>> maybe = List.of(Optional.of("React"), Optional.empty());
List<String> names = maybe.stream()
    .flatMap(Optional::stream) // Java 9+
    .toList();
```

前端：`arr.map(...).flat()` 或直接 `flatMap`。

---

## 5.6 副作用与并行流

中间操作尽量纯。写库、发 HTTP、打复杂日志：慎进 stream，常不如普通 for 清晰。

`parallelStream()` 适合：CPU 密集、无共享可变、数据量大到抵得过调度成本。  

不适合：DB / Redis / HTTP（打爆连接池）、共享 `ArrayList.add`、事务边界里乱并行。

```java
// 并行里抢同一个 ArrayList → 数据竞争
List<String> sink = new ArrayList<>();
list.parallelStream().forEach(sink::add);

// 让 collect 帮你收
List<String> ok = list.parallelStream().map(...).toList();
```

公共池是 `ForkJoinPool.commonPool()`——和 Node 里开几个 Promise 不是一个资源模型。模块二讲线程池后再回来看。

---

## 5.7 调试与受检异常

- 断点难跟：临时 `peek(System.out::println)`  
- Lambda 里抛受检异常很烦：包装成 RuntimeException，或退回 for  
- 同一 Stream 用两次 → `IllegalStateException`：先 collect 成 List 再多次处理  

```java
var stream = list.stream().map(String::trim);
stream.toList();
// stream.toList(); // 第二次炸
```

---

## 5.8 先自测

1. 为啥说 Stream 是惰性的？什么触发计算？  
2. 为啥 Stream 不能复用？  
3. 什么时候用 `groupingBy` 而不是手写 for？  
4. `map` 和 `flatMap` 差在哪？  
5. 为啥 IO 密集别用 `parallelStream`？

---

## 5.9 动手

```bash
mvn -pl 01-Java-Core-And-OOP exec:java -Dexec.mainClass="com.jffd.core.stream.StreamDemo"
```

重点看：`peek` 证明短路；`groupingBy`；`Optional.stream` 摊平。

---

## 避坑

1. Stream 用两次  
2. 并行流 + 共享可变集合  
3. stream 里做远程调用 / 开事务  
4. `map` 出 null 再下游 NPE  
5. 简单 for 硬写成不可维护管道  

## 面试

- 中间操作与终端操作？惰性求值？  
- `map` 与 `flatMap`？  
- 并行流原理与适用/禁用场景？  
- Lambda 与匿名内部类（this、final 捕获）？  
- `Collectors.toList()` 与 `.toList()` 差异？

下一章 → [06-exception-system.md](./06-exception-system.md)
