# 模块一 · Java 核心与 OOP

本模块对应 Learn 课程里的 **Getting started + Core**：先把 JDK 跑通，再按顺序学类型、面向对象、集合、泛型、Stream 与异常。

写法对齐 [MDN Learn](https://developer.mozilla.org/zh-CN/docs/Learn_web_development) 的课程序列与文章骨架（前置 → 学完应能 → 台阶正文 → 检验 / 动手 → 小结）。全书约定见 [guide.md](/guide)。本地对照源码目录：`D:\ateng\MDN\content\files\en-us\learn_web_development`。

目标不是「一次变成专家」，而是 **从不会到够用**——学完后能读进阶资料、能跑 Demo、能解释核心概念。

## 怎么读

0. 还没装 Java？从第 0 章开始。  
1. 按下面教程顺序读；写过多年前端也不要跳台阶。  
2. 每章先对照「学完应能」与「检验一下」，再跑 Demo。  
3. 「避坑 / 面试」放在概念之后，最后扫。

## 教程与挑战（按顺序）

### Getting started

- [0. 安装 JDK 与工具链](./00-install-jdk-and-toolchain.md)  
  - : 装好 JDK 17 与 Maven，编译并跑通第一个 Demo。

### Core

- [1. 强类型与基础语法](./01-strong-typing-and-basics.md)  
  - : 六个知识要点（各含 MDN 六段式）：强类型与变量 → 基本/包装类型 → 转换与控制流 → 相等比较 → `final`/集合/方法 → 空值与 `String`。  
- [2. 面向对象深挖](./02-oop-deep-dive.md)  
  - : 封装、组合与接口、多态、`equals`/`hashCode`、`record`。  
- [3. 集合框架](./03-collections-framework.md)  
  - : `List`/`Set`/`Map` 选型、`HashMap` 契约、fail-fast。  
- [4. 泛型](./04-generics.md)  
  - : 泛型声明、PECS、类型擦除与限制。  
- [5. Stream 与 Lambda](./05-stream-and-lambda.md)  
  - : 函数式接口、惰性管道、`collect`、并行边界。  
- [6. 异常体系](./06-exception-system.md)  
  - : 受检/非受检、try-with-resources、业务异常与 cause。

源码根目录：`01-Java-Core-And-OOP/src/main/java/com/jffd/core/`（各章文首有对应 `*Demo.java`）

| # | 建议耗时 | 示例主类 |
|---|----------|----------|
| 0 | 0.5~1h | （环境验收） |
| 1 | 2.5~3.5h | `com.jffd.core.typing.StrongTypingDemo` |
| 2 | 2h | `com.jffd.core.oop.OopDemo` |
| 3 | 2~2.5h | `com.jffd.core.collections.CollectionsDemo` |
| 4 | 1.5h | `com.jffd.core.generics.GenericsDemo` |
| 5 | 2h | `com.jffd.core.stream.StreamDemo` |
| 6 | 1.5h | `com.jffd.core.exception.ExceptionDemo` |

## 检验进度

学完 Core 后，应能勾选第 6 章文末的「模块一收官」清单。卡住某章时，回到该章「前置」与「学完应能」，不要靠前端类比硬跳。

## 快速运行

先确认是 17（本机若默认仍是 8，见第 0 章）：

```powershell
$env:JAVA_HOME = "C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot"
$env:Path = "$env:JAVA_HOME\bin;" + $env:Path
java -version
```

在仓库根目录：

```bash
mvn -pl 01-Java-Core-And-OOP -am compile

mvn -pl 01-Java-Core-And-OOP exec:java \
  -Dexec.mainClass="com.jffd.core.typing.StrongTypingDemo"
```

## 迁移提示（辅线，读完对应章再看）

| 你习惯的 | Java 里要改成 |
|----------|----------------|
| 装 Node LTS | 装 **JDK 17** |
| `let x: number` | 先分清 `int` 与 `Integer`（见第 1 章） |
| `const` | `final`（只锁引用） |
| 结构类型 | 名义类型：显式 `implements` |
| `===` | 引用用 `==`；内容用 `equals` |
| `any` | 编译期拦住；别靠断言糊弄 |

下一章 → [00-install-jdk-and-toolchain.md](./00-install-jdk-and-toolchain.md)
