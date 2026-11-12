# 模块一 · Java 核心与 OOP

> **前端一句话**：先装好 JDK 17（≈ 装 Node LTS），再把 TypeScript `strict: true` 拧紧一档——值类型 / 引用类型在运行时真有区别，也没有「对象字面量随便塞字段」的自由。

## 怎么读

0. **还没装 Java？** 先读第 0 章，把 `java -version` 变成 17，再编译本模块。  
1. 再把后续章节 Markdown 读完（含自测），类比和坑点吃透。  
2. 打开对应 `*Demo.java`，或 `mvn exec:java` 跑一遍。  
3. 章末「避坑 / 面试」扫一眼就行，先别死磕源码细节。

本模块对应仓库第一步交付内容。读完你应能：

- 本机 JDK 17 + Maven 可用，并能跑通模块一 Demo
- 用 Java 写出带泛型的集合处理代码（≈ 熟练的 TS `Array`/`Map`）
- 理解 `equals`/`hashCode`、接口与抽象类的选型（≈ 类型系统 + 设计取舍）
- 用 Stream 做数据管道（≈ `map/filter/reduce`，但有惰性与并行差异）
- 正确处理受检异常与 NPE（≈ 比 TS 更「强迫你处理失败路径」）

---

## 章节导航

| # | 章节 | 建议耗时 | 示例主类 |
|---|------|----------|----------|
| 0 | [安装 JDK 与工具链](./00-install-jdk-and-toolchain.md) | 0.5~1h | （环境验收 + 可选 Hello） |
| 1 | [强类型与基础语法](./01-strong-typing-and-basics.md) | 1.5h | `com.jffd.core.typing.StrongTypingDemo` |
| 2 | [面向对象深挖](./02-oop-deep-dive.md) | 2h | `com.jffd.core.oop.OopDemo` |
| 3 | [集合框架](./03-collections-framework.md) | 2.5h | `com.jffd.core.collections.CollectionsDemo` |
| 4 | [泛型](./04-generics.md) | 1.5h | `com.jffd.core.generics.GenericsDemo` |
| 5 | [Stream 与 Lambda](./05-stream-and-lambda.md) | 2h | `com.jffd.core.stream.StreamDemo` |
| 6 | [异常体系](./06-exception-system.md) | 1.5h | `com.jffd.core.exception.ExceptionDemo` |

源码根目录：`01-Java-Core-And-OOP/src/main/java/com/jffd/core/`（在 IDE 中打开；各章文首有对应 `*Demo.java` 链接）

---

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

Windows PowerShell 同一条命令即可（注意引号）。

---

## TS → Java 切换清单（贴显示器）

| 你习惯的 | Java 里要改成 |
|----------|----------------|
| 装 Node LTS | 装 **JDK 17**（不是 JRE，不是 8） |
| `nvm use 18` | 调 `JAVA_HOME` + PATH，让 `java`/`mvn` 都指向 17 |
| `let x: number` | `int x` 或 `Integer x`（装箱有成本与 NPE） |
| `const` | `final`（引用不可变，≠ 深不可变） |
| `interface` 可有可选字段 | Java `interface` 是行为契约；数据用 `record`/`class` |
| 结构类型（鸭子类型） | **名义类型**：必须显式 `implements` / 继承 |
| `===` | 引用用 `==`；内容相等用 `equals`（大坑） |
| `undefined` / 缺字段 | 基本没有；只有 `null`，且基本类型不能为 null |
| `any` / 断言糊弄过去 | 编译期拦住；反射/原始类型才能「逃逸」 |
| `async/await` 单线程 | 真正的多线程（模块二）；这里先建立「阻塞调用」直觉 |
| `npm i lodash` | 优先标准库；第三方进 `pom.xml` |

下一章 → [00-install-jdk-and-toolchain.md](./00-install-jdk-and-toolchain.md)
