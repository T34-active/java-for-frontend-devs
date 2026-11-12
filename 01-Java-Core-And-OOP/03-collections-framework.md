# 3. 集合框架

本章讨论 Java 集合框架：`List`、`Set`、`Queue`、`Map` 的接口关系，常用实现如何选型，以及遍历时的 fail-fast、不可变集合和 `Map.get` 的 null 歧义。

对应代码：[`CollectionsDemo.java`](./src/main/java/com/jffd/core/collections/CollectionsDemo.java)

| | |
|--|--|
| 前置 | 第 1–2 章：引用类型、`equals`/`hashCode`、为何是 `List<Integer>`。 |
| 学完应能 | 画出 Collection / Map 族谱；默认选用 `ArrayList`/`HashMap`；解释 fail-fast 与可变 key；空集合不返回 null。 |

下面从接口族谱开始，按顺序读。

---

## 3.1 集合接口族谱

Java 集合主要分两支：`Collection`（List / Set / Queue）与独立的 `Map`。

![集合接口族谱](./assets/collection-hierarchy.svg)

写变量类型时，尽量依赖接口，而不是写死实现类：

```java
List<String> list = new ArrayList<>();
Map<String, Integer> map = new HashMap<>();
```

日常最常用：`ArrayList`、`HashMap`、`HashSet`、`ArrayDeque`。并发场景下的 `ConcurrentHashMap` 放在模块二。

---

## 3.2 `List` 与 `ArrayList`

**`List`** 是有序列表接口。业务里最常见的实现是 **`ArrayList`**：底层是可扩容的数组。

![ArrayList 底层结构](./assets/arraylist-structure.svg)

```java
List<String> list = new ArrayList<>();
list.add("a");
list.add("b");
String first = list.get(0);
```

操作代价（量级直觉）：

| 操作 | 大致复杂度 | 说明 |
|------|------------|------|
| 尾部 `add` | 摊还 O(1) | 偶尔扩容会拷贝数组 |
| 中间 `add` / `remove` | O(n) | 需要搬移元素 |
| `get(i)` | O(1) | 按下标访问 |
| `contains` | O(n) | 通常要扫描 |

已知大概规模时，可以预分配容量，减少扩容：

```java
List<String> list = new ArrayList<>(256);
```

### 为什么业务很少用 `LinkedList`

链表在「头尾插入」上理论好看，但节点分散、缓存不友好，对象头开销也大。真正要队列语义时，更常用 `ArrayDeque`。面试可以说清 `LinkedList` 特点；写业务默认 `ArrayList`。

---

## 3.3 `Map` 与 `HashMap`

**`Map`** 保存键到值的映射。最常用的实现是 **`HashMap`**。

```java
Map<String, Integer> stars = new HashMap<>();
stars.put("react", 220_000);
stars.putIfAbsent("vue", 1);
int v = stars.getOrDefault("angular", 0);
```

### 结构直觉（JDK 8+）

![HashMap 桶与查找](./assets/hashmap-buckets.svg)

放入或查找时大致步骤：计算 hash → 落到某个桶 → 在桶内用 `equals` 判断是不是同一个键。元素过多、超过「负载因子 × 容量」（默认负载因子 0.75）时扩容。

面试常背的经验值：链表长度 ≥ 8 且数组长度 ≥ 64 时可能树化。先建立心智即可，不必死记实现细节。

### 键的要求

`HashMap` 的键可以是任意对象，但键的相等性依赖 `hashCode` 与 `equals`。因此：

- 用作键的类应正确实现这两者。  
- 键放入后，不要再修改参与 `hashCode`/`equals` 的字段。

可变键的典型事故：

![可变键导致 HashMap 丢失](./assets/mutable-key-pitfall.svg)

键优先使用不可变类型：`String`、`Long`、`record`、枚举等。
### 线程安全

`HashMap` **不是**线程安全的。多线程同时写入可能丢数据或出现更糟的情况。并发场景用 `ConcurrentHashMap`（模块二）。

---

## 3.4 `Set` 与其他常用实现

**`Set`** 表示不重复元素的集合。`HashSet` 内部通常借助 `HashMap` 的键来实现去重。

```java
Set<String> tags = new HashSet<>();
tags.add("java");
tags.add("java"); // size 仍为 1
```

| 类型 | 特征 | 典型用途 |
|------|------|----------|
| `LinkedHashMap` | 保持插入序（可配置为访问序） | 需要顺序的 Map；简易 LRU |
| `TreeMap` | 按键排序 | 有序键、范围查询 |
| `HashSet` | 去重 | 唯一集合 |
| `LinkedHashSet` | 去重且保持插入序 | 唯一且要顺序 |
| `ArrayDeque` | 双端队列 | 队列、栈（不要用过时的 `Stack` 类） |

---

## 3.5 遍历与 fail-fast

在用增强 for 遍历时，如果直接对底层集合做结构性修改（例如 `list.remove`），常会抛出 **`ConcurrentModificationException`（CME）**。这叫 **fail-fast**：尽快失败，避免静默错乱。

```java
List<String> list = new ArrayList<>(List.of("a", "b", "c"));

// 错误示范：增强 for 里结构性删除
// for (String s : list) {
//     if (s.equals("b")) list.remove(s);
// }

list.removeIf(s -> s.equals("b")); // 推荐
```

也可以使用迭代器自己的 `remove()`。现代代码优先 `removeIf`。

---

## 3.6 不可变集合与返回值

```java
List<String> freeze = List.of("x", "y");
Map<String, Integer> m = Map.of("a", 1);
```

- 「没有数据」时返回 `List.of()` 或 `Collections.emptyList()`，不要返回 `null`。  
- 需要防止调用方修改时，返回不可变集合或不可变副本。  
- `subList` 是**视图**：改原列表会影响子列表，不要把它当成独立深拷贝。

---

## 3.7 `Map.get` 得到 `null` 的歧义

```java
Integer v = map.get(k);
// null 可能表示：没有这个键，或值本身就是 null
```

处理方式包括：`containsKey`、`getOrDefault`、禁止存 null 值，或按团队约定使用 `Optional`。

---

## 检验一下

1. 为什么业务默认用 `ArrayList` 而不是 `LinkedList`？  
2. `HashMap` 何时扩容？树化的大致条件是什么？  
3. 为什么用作 Map 键的类需要正确的 `equals`/`hashCode`？  
4. CME 通常在什么情况下出现？正确删除方式是什么？  
5. 接口返回空列表为什么比返回 `null` 更好？

---

## 动手

1. 运行：

```bash
mvn -pl 01-Java-Core-And-OOP exec:java -Dexec.mainClass="com.jffd.core.collections.CollectionsDemo"
```

2. 重点观察末尾可变 key：修改 key 后 `get` 变为 null，但 `containsValue` 仍可能为 true。

---

## 避坑

1. 大列表频繁 `contains`，或频繁在中间插入  
2. 多线程共用 `HashMap` 写入  
3. 可变对象当 key  
4. 增强 for 里直接 `list.remove`  
5. 忽略 `map.get` 的 null 歧义  
6. 把 `subList` 当深拷贝返回

## 面试（可选）

- `ArrayList` 与 `LinkedList`？扩容？  
- `HashMap` 结构、`put`、扩容、树化？  
- `HashMap` 与 `ConcurrentHashMap`？  
- fail-fast 与 fail-safe？  
- `hashCode` / `equals` 如何影响 `HashMap`？  
- 如何用 `LinkedHashMap` 实现简易 LRU？

## 小结

你已经能按接口选型集合，并知道 `HashMap` 依赖键的相等契约、遍历时不要乱改结构。下一章解释 `List<String>` 这种尖括号在编译期和运行期分别意味着什么。

下一章 → [04-generics.md](./04-generics.md)
