# Java For Frontend Devs

> 写给**有经验的前端工程师**的 Java 全栈/后端系统化学习仓库。  
> 目标：跳过「什么是变量/循环」，用你熟悉的 **JS/TS/React/Vue/Node** 心智模型，直击 Java 与企业级后端的思维差异。

## 文档站（VitePress）

```bash
npm install
npm run docs:dev      # http://localhost:6100 （已开 --host；勿用 6000，Chrome 会 ERR_UNSAFE_PORT）
npm run docs:build    # 输出到 .vitepress/dist
```

像看书一样从左侧目录读；Java 示例仍在各模块 `src/` 下用 Maven 运行。

---

## 你将获得什么

| 维度 | 说明 |
|------|------|
| 前端类比 | 每个概念都有「≈ 前端的某某」锚点，降低切换成本 |
| 代码即文档 | 章节 Markdown + 旁边 `src/` 可运行示例一一对应 |
| 生产避坑 | NPE、循环依赖、事务失效、缓存三大问题等高频坑 |
| 面试考点 | 每章末尾「高频面试」小节，方便边学边背 |

**前置假设**：你会 TypeScript、Promise/async、npm、组件化、状态管理、HTTP/REST。JDK 建议 **17+**，构建工具 **Maven 3.9+**。

---

## 工具链心智对照（先建立全局地图）

| Java / 后端 | 前端熟悉物 | 一句话 |
|-------------|-----------|--------|
| JDK | Node.js 运行时 | 语言 + 标准库 + 虚拟机 |
| Maven / Gradle | npm / pnpm + Vite | 依赖、脚本、打包 |
| `pom.xml` | `package.json` | 坐标、依赖、插件 |
| JAR / WAR | 打包后的 `dist` | 可部署产物 |
| Spring Boot | NestJS / 约定大于配置的 Node 框架 | 快速搭 Web 服务 |
| IoC 容器 | DI + Context（React Context / Nest 注入） | 对象由容器创建与装配 |
| AOP | 装饰器 / 中间件横切 | 日志、事务、鉴权切面 |
| Servlet Filter / Interceptor | Express/Koa 中间件 | 请求进出管道 |
| MyBatis / JPA | Prisma / TypeORM | SQL 映射或 ORM |
| Redis | 内存 KV / 分布式 session | 缓存与分布式协作 |
| RabbitMQ | 消息队列 / 事件总线 | 异步解耦 |
| JWT + Sa-Token | Cookie/Session + 前端鉴权库 | 前后端分离登录态 |
| Docker | 可复现的运行环境镜像 | 部署一致性 |

---

## 全书目录与学习路线

建议顺序：**自上而下、边读边跑**。每个模块读完再进下一模块；模块内按编号章节推进。

```text
Java_For_Frontend_Devs/
├── README.md                          ← GitHub 总目录（本文件）
├── index.md / guide.md                ← VitePress 首页与路线图
├── .vitepress/config.mts              ← 文档站侧边栏与主题
├── package.json                       ← npm run docs:dev
├── pom.xml                            ← 父工程（Spring Boot 3.3.x BOM）
├── 01-Java-Core-And-OOP/              ✅ 第一步已完整交付
├── 02-Concurrency-And-JVM/            ⏳ 待生成
├── 03-SpringBoot-Ecosystem/           ⏳ 待生成
├── 04-Database-And-ORM/               ⏳ 待生成
└── 05-Middleware-And-Architecture/    ⏳ 待生成
```

### 模块一 · Java 核心与 OOP ✅

路径：[`01-Java-Core-And-OOP/`](./01-Java-Core-And-OOP/)

| 章节 | 文件 | 前端锚点 |
|------|------|----------|
| 导读 | [index.md](./01-Java-Core-And-OOP/index.md) | TS → Java 切换清单 |
| 0. 安装 JDK 与工具链 | [00-install-jdk-and-toolchain.md](./01-Java-Core-And-OOP/00-install-jdk-and-toolchain.md) | 装 Node LTS / nvm 换版本 |
| 1. 强类型与基础语法 | [01-strong-typing-and-basics.md](./01-Java-Core-And-OOP/01-strong-typing-and-basics.md) | `strict` TS、primitive vs object |
| 2. 面向对象深挖 | [02-oop-deep-dive.md](./01-Java-Core-And-OOP/02-oop-deep-dive.md) | class/interface、组合优于继承 |
| 3. 集合框架（含源码心智） | [03-collections-framework.md](./01-Java-Core-And-OOP/03-collections-framework.md) | Array/Map/Set + 复杂度 |
| 4. 泛型 | [04-generics.md](./01-Java-Core-And-OOP/04-generics.md) | TS Generics、擦除差异 |
| 5. Stream 与 Lambda | [05-stream-and-lambda.md](./01-Java-Core-And-OOP/05-stream-and-lambda.md) | `map/filter/reduce`、惰性求值 |
| 6. 异常体系 | [06-exception-system.md](./01-Java-Core-And-OOP/06-exception-system.md) | try/catch、Error Boundary 类比 |

### 模块二 · 并发与 JVM ⏳

路径：`02-Concurrency-And-JVM/`（占位，待你指示后生成）

预告：线程池实战、synchronized/ReentrantLock、volatile、JMM、GC 基础 —— 全程对比 **浏览器事件循环 / Worker / 单线程模型**。

### 模块三 · Spring Boot 生态 ⏳

路径：`03-SpringBoot-Ecosystem/`

预告：IoC/AOP、RESTful、统一响应、全局异常、Validation、Filter/Interceptor。

### 模块四 · 数据库与 ORM ⏳

路径：`04-Database-And-ORM/`

预告：MySQL 索引与隔离级别、MyBatis-Plus、联表与 SQL 优化。

### 模块五 · 中间件与架构 ⏳

路径：`05-Middleware-And-Architecture/`

预告：Redis 三大问题与分布式锁、RabbitMQ、JWT+Sa-Token、Docker 部署。

---

## 环境准备（从安装 Java 开始）

完整步骤（装 JDK 17、修 PATH、Maven、IDE、验收命令）见：

→ [**00-install-jdk-and-toolchain.md**](./01-Java-Core-And-OOP/00-install-jdk-and-toolchain.md)

速查（本机若默认仍是 JDK 8，先切到 17）：

```powershell
$env:JAVA_HOME = "C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot"
$env:Path = "$env:JAVA_HOME\bin;" + $env:Path
java -version
mvn -version

mvn -pl 01-Java-Core-And-OOP -am compile
mvn -pl 01-Java-Core-And-OOP exec:java "-Dexec.mainClass=com.jffd.core.typing.StrongTypingDemo"
```

IDE：IntelliJ IDEA（推荐）或 VS Code + Extension Pack for Java；Project SDK 选 **17**。

---

## 学习方法建议

1. **先完成第 0 章**：JDK 17 + Maven，能 `compile` 再往下读  
2. **先读 Markdown 类比段**，确认「这不就是前端的 X」  
3. **再盯注释跑 Demo**，改几行看编译器怎么骂你（Java 的严格是特性）  
4. **每章「避坑 / 面试」扫一眼**，用 Anki 或笔记摘 3 条即可  
5. 读完模块一后回复：「继续模块二」，我会按同样标准生成下一章  

---

## 版本与约定

- Java：**17**（Spring Boot 3.x 最低要求）  
- Spring Boot：**3.3.x**（后续模块）  
- 包名前缀：`com.jffd.*`（Java For Frontend Devs）  
- 文档语言：简体中文；代码标识符：英文  

祝切换顺利。文档站：`npm run docs:dev`；学习从 [安装 JDK](./01-Java-Core-And-OOP/00-install-jdk-and-toolchain.md) 开始，或读 [`01-Java-Core-And-OOP/index.md`](./01-Java-Core-And-OOP/index.md)。
