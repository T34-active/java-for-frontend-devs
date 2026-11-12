# Java For Frontend Devs

写给**有经验前端工程师**的 Java 全栈 / 后端系统化学习仓库。  
跳过「什么是变量 / 循环」，用你熟悉的 **JS / TS / React / Vue / Node** 心智模型，直击 Java 与企业级后端的思维差异。

| 入口 | 地址 |
|------|------|
| 在线文档（GitHub Pages） | https://t34-active.github.io/java-for-frontend-devs/ |
| 源码仓库 | https://github.com/T34-active/java-for-frontend-devs |

## 项目是什么

这是一套「课程序列」式教材，不是碎片对照表：

- **Markdown 讲概念** + 旁边 `src/` **可运行 Java Demo**（代码即文档）
- 每个知识点按 MDN Learn 六段式写：概述 → 心智模型 → 语法 → 示例 → 避坑 → 前后端对照
- 目标读者：会 TypeScript、组件化、HTTP/REST，准备切入 Java / Spring 后端

**前置**：JDK **17+**，Maven **3.9+**；本地文档站用 Node 20 + npm。

## 本地跑文档站

```bash
npm install
npm run docs:dev      # http://localhost:6100（勿用 6000，Chrome 会 ERR_UNSAFE_PORT）
npm run docs:build    # 输出到 .vitepress/dist
```

## 协作与流水线

推荐流程：**开分支 → 提 PR → 等 CI 绿灯 → 你自己合并 `main`**。

| 时机 | 流水线 | 做什么 |
|------|--------|--------|
| 打开 / 更新 PR | `CI` | 构建 VitePress；编译模块一 Java Demo |
| 合并进 `main`（或手动触发） | `Deploy docs` | 构建文档并发布到 GitHub Pages |

合并后几分钟内更新：https://t34-active.github.io/java-for-frontend-devs/

## 你会学到什么

| 维度 | 说明 |
|------|------|
| 前端类比 | 每个概念有「≈ 前端的某某」锚点，降低切换成本 |
| 代码即文档 | 章节 Markdown 与 `src/` Demo 一一对应，可 `mvn` 跑 |
| 生产避坑 | NPE、循环依赖、事务失效、缓存三大问题等高频坑 |
| 可自检目标 | 每章 Learning outcomes + 自测；面试考点作可选附录 |

## 工具链心智对照

| Java / 后端 | 前端熟悉物 | 一句话 |
|-------------|-----------|--------|
| JDK | Node.js 运行时 | 语言 + 标准库 + 虚拟机 |
| Maven / Gradle | npm / pnpm + Vite | 依赖、脚本、打包 |
| `pom.xml` | `package.json` | 坐标、依赖、插件 |
| JAR / WAR | 打包后的 `dist` | 可部署产物 |
| Spring Boot | NestJS / 约定大于配置的框架 | 快速搭 Web 服务 |
| IoC 容器 | DI + Context | 对象由容器创建与装配 |
| AOP | 装饰器 / 中间件横切 | 日志、事务、鉴权切面 |
| MyBatis / JPA | Prisma / TypeORM | SQL 映射或 ORM |
| Redis | 内存 KV | 缓存与分布式协作 |
| RabbitMQ | 消息队列 / 事件总线 | 异步解耦 |

## 学习路线

建议顺序：**自上而下、边读边跑**。

```text
Java_For_Frontend_Devs/
├── README.md                          ← 本文件（GitHub 总览）
├── index.md / guide.md                ← VitePress 首页与写作约定
├── .vitepress/                        ← 文档站配置与构建产物
├── package.json                       ← npm run docs:dev / docs:build
├── pom.xml                            ← 父工程（Spring Boot 3.3.x BOM）
├── 01-Java-Core-And-OOP/              ✅ 已交付
├── 02-Concurrency-And-JVM/            ⏳ 待生成
├── 03-SpringBoot-Ecosystem/           ⏳ 待生成
├── 04-Database-And-ORM/               ⏳ 待生成
└── 05-Middleware-And-Architecture/    ⏳ 待生成
```

### 模块一 · Java 核心与 OOP ✅

| 章节 | 前端锚点 |
|------|----------|
| [0. 安装 JDK 与工具链](./01-Java-Core-And-OOP/00-install-jdk-and-toolchain.md) | 装 Node LTS / nvm 换版本 |
| [1. 强类型与基础语法](./01-Java-Core-And-OOP/01-strong-typing-and-basics.md) | `strict` TS、primitive vs object |
| [2. 面向对象深挖](./01-Java-Core-And-OOP/02-oop-deep-dive.md) | class / interface、组合优于继承 |
| [3. 集合框架](./01-Java-Core-And-OOP/03-collections-framework.md) | Array / Map / Set + 复杂度 |
| [4. 泛型](./01-Java-Core-And-OOP/04-generics.md) | TS Generics、擦除差异 |
| [5. Stream 与 Lambda](./01-Java-Core-And-OOP/05-stream-and-lambda.md) | `map` / `filter` / `reduce` |
| [6. 异常体系](./01-Java-Core-And-OOP/06-exception-system.md) | try/catch、Error Boundary 类比 |

### 后续模块（占位）

- **模块二 · 并发与 JVM**：线程池、锁、JMM、GC —— 对照事件循环 / Worker  
- **模块三 · Spring Boot**：IoC / AOP、REST、校验、Filter / Interceptor  
- **模块四 · 数据库与 ORM**：MySQL、MyBatis-Plus、事务与 SQL 优化  
- **模块五 · 中间件与架构**：Redis、RabbitMQ、JWT + Sa-Token、Docker  

## 跑 Java 示例（模块一）

完整安装步骤见 [00-install-jdk-and-toolchain.md](./01-Java-Core-And-OOP/00-install-jdk-and-toolchain.md)。

```powershell
java -version   # 需 17+
mvn -version

mvn -pl 01-Java-Core-And-OOP -am compile
mvn -pl 01-Java-Core-And-OOP exec:java "-Dexec.mainClass=com.jffd.core.typing.StrongTypingDemo"
```

## 版本与约定

- Java **17**（Spring Boot 3.x 最低要求）
- Spring Boot **3.3.x**（后续模块）
- 包名前缀：`com.jffd.*`（Java For Frontend Devs）
- 文档：简体中文；代码标识符：英文

从 [安装 JDK](./01-Java-Core-And-OOP/00-install-jdk-and-toolchain.md) 开始，或打开在线文档：https://t34-active.github.io/java-for-frontend-devs/
