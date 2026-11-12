# 全书总览与学习路线

> 本页是 VitePress 站点内的「书目」；仓库根目录的 `README.md` 面向 GitHub/IDE 阅读，内容同源思路。

## 你将获得什么

| 维度 | 说明 |
|------|------|
| 前端类比 | 每个概念都有「≈ 前端的某某」锚点 |
| 代码即文档 | 章节 Markdown + 旁边 `src/` 可运行示例 |
| 生产避坑 | NPE、循环依赖、事务失效、缓存三大问题等 |
| 面试考点 | 每章末尾「高频面试」小节 |

**前置**：熟练 TypeScript / 组件化 / HTTP。学习顺序：**先装 JDK 17**，再读语法。

## 工具链心智对照

| Java / 后端 | 前端熟悉物 | 一句话 |
|-------------|-----------|--------|
| JDK | Node.js 运行时 | 语言 + 标准库 + 虚拟机 |
| Maven | npm / pnpm | 依赖与构建 |
| Spring Boot | NestJS | 约定大于配置的 Web 框架 |
| IoC | DI / Context | 对象由容器装配 |
| MyBatis-Plus | Prisma / TypeORM | 持久层 |
| Redis / MQ | 缓存与事件总线 | 分布式协作 |

## 模块导航

| 模块 | 状态 | 入口 |
|------|------|------|
| 01 Java 核心与 OOP | ✅ 已交付 | [进入](/01-Java-Core-And-OOP/) · 从 [安装 JDK](/01-Java-Core-And-OOP/00-install-jdk-and-toolchain) 开始 |
| 02 并发与 JVM | ⏳ 待生成 | [占位](/02-Concurrency-And-JVM/) |
| 03 Spring Boot 生态 | ⏳ 待生成 | [占位](/03-SpringBoot-Ecosystem/) |
| 04 数据库与 ORM | ⏳ 待生成 | [占位](/04-Database-And-ORM/) |
| 05 中间件与架构 | ⏳ 待生成 | [占位](/05-Middleware-And-Architecture/) |

## 本地跑文档站

```bash
npm install
npm run docs:dev
```

浏览器打开终端提示的本地地址（默认 `http://localhost:6100`，已开 `--host`；不要用 6000，Chrome/Edge 会报 `ERR_UNSAFE_PORT`）。

## 跑 Java 示例

完整安装见 [00 · 安装 JDK 与工具链](/01-Java-Core-And-OOP/00-install-jdk-and-toolchain)。本机若默认仍是 8：

```powershell
$env:JAVA_HOME = "C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot"
$env:Path = "$env:JAVA_HOME\bin;" + $env:Path

mvn -pl 01-Java-Core-And-OOP -am compile
mvn -pl 01-Java-Core-And-OOP exec:java "-Dexec.mainClass=com.jffd.core.typing.StrongTypingDemo"
```

下一篇 → [模块一导读](/01-Java-Core-And-OOP/) · 或直接 [安装 JDK](/01-Java-Core-And-OOP/00-install-jdk-and-toolchain)
