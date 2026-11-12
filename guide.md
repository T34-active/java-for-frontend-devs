# 全书总览与学习路线

> 本页是 VitePress 站点内的「书目」；仓库根目录的 `README.md` 面向 GitHub/IDE 阅读，内容同源思路。

## 写作约定（学 MDN Learn，不是学「速成对照表」）

两套官方教材一起学：

- [MDN JavaScript 指南](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide) — 语言概述的台阶写法  
- 本地源：`D:\ateng\MDN\content\files\en-us\learn_web_development` — **Learn 课程**的课程序列（Getting started → Core → Extensions）

目标对齐 Learn：**从不会到「够用、能查进阶资料」**，不是从零到专家。读者可能写过多年前端，但 Java 基础仍要一步一步建，不能用「≈ TS 的某某」把台阶拆掉。

### 路线结构（学 Learn 的三层）

| 层 | 对应本仓库 | 作用 |
|----|------------|------|
| Getting started | 模块一第 0 章 | 环境、第一次跑通 |
| Core | 模块一 1–6 章，以及后续模块主干 | 必学主干，按顺序 |
| Extensions / 深水 | 章内「备注」、面试加分、专章外链 | 学完 Core 再钻 |

### 每一章必须有的骨架（学 Learn 文章页）

1. **开篇一句**：本章讨论什么（圈范围）。  
2. **Prerequisites / 前置**：读本章前应已会什么；写了仍从零讲本章概念。  
3. **Learning outcomes / 学完应能**：具体可检查的条目（会解释 X、会写出 Y），不是空泛「掌握 OOP」。  
4. **正文**：按「核心知识点」推进；知识点之间必须有前因后果桥接，禁止碎片清单。  
5. **主动练习**：动手步骤编号（先跑什么、再观察什么）。  
6. **Summary / 小结**：用几句话收束本章，再链下一章。

### 每个核心知识点的 MDN 六段式（强制）

每一个独立知识点（不是整章糊成一段，也不是拆成十几条碎节）都必须按此顺序写满，不得缺段、不得把对照表提前抢戏：

1. **概述 (Overview)** — 大白话说明「为什么需要它」；没有它会遇到什么麻烦；再给核心定位。可用精确的前端类比帮助迁移，但类比不能替代 Java 自己的定义。  
2. **底层心智模型 (Mental Model)** — 内存 / 引用 / 对象关系用 **SVG 图**展示（放各章 `assets/`，Markdown 用 `![说明](./assets/xxx.svg)` 嵌入）；流程因果可再配简短分步文字。禁止再用大段框线 ASCII 充当主图。SVG 必须适配亮/暗主题：颜色走 CSS 变量 + `@media (prefers-color-scheme: dark)`；新增或重写图后跑 `assets/_patch_svg_dark.py`（或生成脚本末尾自动打补丁）。站点侧靠 `.vitepress/theme/custom.css` 给 `<img>` 设 `color-scheme`，使 VitePress 手动切黑夜时图也能跟着变。  
3. **语法与核心 API 签名 (Syntax & Parameters)** — 列出标准写法；逐词解释关键字、参数、返回值、修饰符（如 `public` / `static` / `final` / `<T>`）在此处的作用。  
4. **渐进式示例 (Examples)** — 示例 1 最小可运行原型；示例 2 贴近后端真实场景；每个代码块下方必须有 `// 控制台输出：` 与逐行执行说明。  
5. **常见错误与避坑指南 (Common Pitfalls)** — 2～3 组 `❌` / `✅`，并解释编译错误或异常的根因。  
6. **前端 vs Java 快速对照表 (Comparison)** — 放在该知识点末尾，汇总写法、类型安全与运行时差异。

### 正文纪律

1. **少而完整**：一章只设少数「核心知识点」，每个写满六段；禁止切成无因果的碎标题。  
2. **先因后果**：下一知识点必须回答「上一节解决了什么、还缺什么」。  
3. **先模型后语法再示例**：心智模型讲清后，再给签名与代码。  
4. **深水区外链**：擦除、源码细节链到专章或「备注」，本章不提前卸载。  
5. **Test your skills ≠ 面试题堆砌**：自测先检验「学完应能」；面试题可附在后作可选。

### 参考 JavaGuide 的融合约定

深度与常见考点可参考开源项目 [JavaGuide](https://github.com/Snailclimb/JavaGuide)（[在线阅读](https://javaguide.cn)，Apache-2.0）。融合时遵守：

1. **受众不变**：仍是「前端转 Java」的 Learn 台阶，不是把本仓库改成面试百科。  
2. **用自己的话重写**：吸收机制结论与易错点，改写成 MDN 六段式知识要点；禁止整段原文搬运。  
3. **署名**：章首或章末「参考」写明对应 JavaGuide 篇目链接。  
4. **深水区外链**：反射、动态代理、完整源码逐行、并发容器等放「备注 + 外链」，不塞进 Core 主台阶。  
5. **面试节可选**：章末「面试（可选）」可增补精选问法并回链 JavaGuide；自测清单仍先检验「学完应能」。

### 行内术语（点按释义）

模块一文中带点状下划线的词可点开短释义（交互类似「高性价比人生指南」里的 CI 提示）。

1. 词条写在 `.vitepress/theme/glossary/module1.ts`；正文用 `<Term id="boxing" />`，或 `<Term id="boxing" text="自动装箱" />`。  
2. **不要**把 `<Term>` 包进行内代码反引号，否则只会当纯文本显示。  
3. **不要**写 `**<Term id="x" />**` 或 `*<Term />*`：Markdown 的加粗/斜体包不住 Vue 组件，页面上会露出 `**`。需要加粗时写 `<Term id="x" strong />`。  
4. 每章首次出现的关键术语再标记即可，不必全文刷屏。  
5. 汇总页：[模块一 · 术语表](/01-Java-Core-And-OOP/glossary)。

### 排版与 `**` 用法（对齐 [zh-CN translation-guide](file:///D:/ateng/MDN/translated-content/docs/zh-cn/translation-guide.md) + MDN Markdown）

参考本地 `D:\ateng\MDN\translated-content\docs\zh-cn\translation-guide.md`，以及 [如何使用 Markdown 撰写文档](https://developer.mozilla.org/zh-CN/docs/MDN/Writing_guidelines/Howto/Markdown_in_MDN)。

1. **中文与拉丁字母 / 数字之间留一个空格**；中文标点与拉丁字母之间不留空格。  
   - 宜：`学习 Java 开发`、`需 10 个小时`、`应用程序接口（API）`  
   - 不宜：`学习Java开发`、`需10个小时`、`（ API ）`
2. **正文标点用中文全角**（代码与类型名内除外）；并列用顿号：`a、b 和 c`。破折号用 `——`。不用「您」，统一用「你」。
3. **`**加粗**` 只强调短词或短语**，不要整句、整段加粗，也不要用加粗冒充小标题。  
   - 宜：`JavaScript 是**区分大小写**的`；首次定义概念时 `**装箱**是指……`  
   - 不宜：`**Java 的强类型（更准确说：静态强类型）做的是同一类事，而且更彻底：……**`
4. **讲 API / 关键字 / 符号本身时，用加粗代码**：`` **`margin`** ``、`` **`final`** ``、`` **`List<Integer>`** ``（与 MDN 参考页一致）。普通行内代码仍用单个反引号 `` `int` ``，不必处处加粗。
5. **正反例不要用 `**❌ 错误写法：**` / `**✅ 正确写法：**` 当标题**。改用四级标题或一两句说明，代码围栏加 MDN 信息字符串：  
   - \`\`\`java example-bad  
   - \`\`\`java example-good  
6. **小节引导语**写成普通句子或真正的 Markdown 标题（`####`），不要写成 `**最小类与入口：**` 这种加粗伪标题。

---

## 你将获得什么

| 维度 | 说明 |
|------|------|
| 课程序列 | 环境 → 类型 → OOP → 集合 → 泛型 → Stream → 异常，台阶不可跳 |
| 代码即文档 | 章节 Markdown + 旁边 `src/` 可运行示例 |
| 生产避坑 | NPE、循环依赖、事务失效、缓存三大问题等（坑在概念之后） |
| 可自检目标 | 每章 Learning outcomes + 自测 + Demo |

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
