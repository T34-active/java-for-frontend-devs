# 3. 集合框架（源码级心智）

> 先搞清选哪种集合、复杂度、fail-fast、HashMap 契约，再跑 Demo。  
> 对应：[`CollectionsDemo.java`](./src/main/java/com/jffd/core/collections/CollectionsDemo.java)

---

## 把 JS 的 Array/Map/Set 映射过来

| 你熟的 | Java 常用 | 备注 |
|--------|-----------|------|
| `Array` | `List` / `ArrayList` | 业务第一公民 |
| `Set` | `HashSet` / `LinkedHashSet` | 去重 |
| `Map` / 对象当字典 | `HashMap` / `LinkedHashMap` | 键可以是任意对象 |
| 队列 / 栈 | `ArrayDeque` | 别用古老的 `Stack` 类 |
| 不可变快照 | `List.of` / `Map.of` | 有点像运行时的 `as const` |

升级点：Java 的 Map 键依赖 `hashCode`/`equals`，不是只有字符串或引用两种简单情况。

---

## 3.1 接口族谱

```text
Iterable
└── Collection
    ├── List     有序、下标、可重复
    ├── Set      不重复（是否有序看实现）
    └── Queue    排队、双端等

Map              独立体系（不是 Collection）
```

尽量依赖接口类型：

```java
List<String> list = new ArrayList<>();
Map<String, Integer> map = new HashMap<>();
```

别到处把参数写成死的 `ArrayList`——跟前端「依赖 Props 接口而不是某个组件类」一个道理。

日常够用：`ArrayList`、`HashMap`、`HashSet`、`ArrayDeque`；并发再加 `ConcurrentHashMap`（模块二）。

---

## 3.2 ArrayList：读源码抓什么

底层就是可扩容数组：

```text
Object[] elementData
int size
```

| 操作 | 复杂度 | 前端直觉 |
|------|--------|----------|
| 尾部 `add` | 摊还 O(1) | `push` |
| 中间 `add/remove` | O(n) | `splice` 搬移 |
| `get(i)` | O(1) | 下标访问 |
| `contains` | O(n) | `includes` 扫一遍 |

容量不够时，常见实现大约扩到 1.5 倍，再 `arraycopy`。已知规模就预分配：

```java
List<String> list = new ArrayList<>(256);
```

### 为啥业务几乎不用 LinkedList

教材爱考链表头插 O(1)。现实是：CPU 更吃连续数组，节点对象开销大，真要队列语义多用 `ArrayDeque`。  
面试可以说 LinkedList 特点，写业务默认 ArrayList。

---

## 3.3 HashMap（必考，也容易出事）

### 结构（JDK 8+）

```text
Node<K,V>[] table
每个桶：链表；太长且容量够大 → 红黑树
```

流程：算 hash → 落到桶 → 桶内用 `equals` 找同 key → 元素太多超过「负载因子 0.75 × 容量」就扩容到约 2 倍。  
树化经验值（面试常背）：链表长度 ≥ 8 且数组长度 ≥ 64 时树化。

### API

```java
Map<String, Integer> stars = new HashMap<>();
stars.put("react", 220_000);
stars.putIfAbsent("vue", 1);
int v = stars.getOrDefault("angular", 0);
stars.forEach((k, val) -> { /* ... */ });
```

| 点 | JS | Java HashMap |
|----|----|--------------|
| 键类型 | 对象引用或字符串为主 | 任意对象，靠 hashCode/equals |
| null key | `Map` 可以 | 允许一个 null key |
| 遍历时删 | 看情况诡异 | 乱删 → `ConcurrentModificationException` |

### 可变 key 陷阱

```text
1. 可变对象当 key put 进去
2. 改了参与 hashCode/equals 的字段
3. get 时算到别的桶 → 变成 null
4. 旧 entry 其实还在（containsValue 可能仍 true）
```

跟「对象当 Map key 然后改对象内容」一个坑。key 用不可变类型：`String`、`Long`、`record`、枚举。

### 线程安全

`HashMap` 不是线程安全的。多线程写可能丢数据；老 JDK 还有死链传说。  
并发用 `ConcurrentHashMap`。`Collections.synchronizedMap` 是粗粒度锁，现代一般不首选。

---

## 3.4 其他常用选型

| 类型 | 特征 | 什么时候用 |
|------|------|------------|
| `LinkedHashMap` | 保持插入序（可配访问序） | 要顺序的 Map；简易 LRU |
| `TreeMap` | 按键排序 | 有序键 / 范围查询 |
| `HashSet` | 内部是 HashMap 的 key | 去重 |
| `LinkedHashSet` | 去重且保插入序 | 唯一 + 顺序 |
| `ArrayDeque` | 双端队列 | 队列、栈 |

```java
Set<String> tags = new HashSet<>();
tags.add("java");
tags.add("java"); // size 仍为 1
```

---

## 3.5 遍历与 fail-fast

```java
List<String> list = new ArrayList<>(List.of("a", "b", "c"));

// enhanced for 里结构性删除 → ConcurrentModificationException
// for (String s : list) {
//     if (s.equals("b")) list.remove(s);
// }

list.removeIf(s -> s.equals("b"));
```

fail-fast：迭代期间结构被改，立刻抛 CME，避免默默错下去。  
前端 `forEach` 里改数组有时还能「看起来能跑」；Java 选择直接报错——这是好事。  
`iterator.remove()` 也安全；`removeIf` 更现代。

---

## 3.6 不可变集合与返回值

```java
List<String> freeze = List.of("x", "y");
Map<String, Integer> m = Map.of("a", 1);
```

- 「没有数据」返回 `List.of()` / `emptyList()`，别返回 null。  
- 需要防外部修改时，返回不可变副本或不可变视图。  
- `subList` 是视图：改原列表会影响子列表，别当独立拷贝。

---

## 3.7 `get` 得到 null 的歧义

```java
Integer v = map.get(k);
// null 可能是：没有这个键，或值就是 null
```

处理：`containsKey`、`getOrDefault`、禁止 null value，或用 Optional 包一层（看团队习惯）。

---

## 3.8 先自测

1. 为啥业务默认 ArrayList 不是 LinkedList？  
2. HashMap 何时扩容？树化大致条件？  
3. 为啥重写 equals 的对象才能当好 Map key？  
4. CME 何时出现？正确删除姿势？  
5. 接口返回空列表为啥比返回 null 好？

---

## 3.9 动手

```bash
mvn -pl 01-Java-Core-And-OOP exec:java -Dexec.mainClass="com.jffd.core.collections.CollectionsDemo"
```

重点看最后的 mutable key：改 key 后 `get` 变 null，但 `containsValue` 仍 true。

---

## 避坑

1. 大列表频繁 `contains` / 中间插入  
2. 并发用 HashMap  
3. 可变对象当 key  
4. foreach 里直接 `list.remove`  
5. `map.get` 的 null 歧义  
6. 把 `subList` 当深拷贝返回  

## 面试

- ArrayList 与 LinkedList？扩容？  
- HashMap 结构、put、扩容、树化？  
- HashMap 与 ConcurrentHashMap？  
- fail-fast 与 fail-safe？  
- hashCode / equals 如何影响 HashMap？  
- 如何实现 LRU？（LinkedHashMap accessOrder）

下一章 → [04-generics.md](./04-generics.md)
