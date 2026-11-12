# 0. 安装 JDK 与工具链

> 先把环境跑通，再谈语法。  
> 目标：本机 `java -version` 显示 **17**，`mvn -version` 也能指向 17，并能编译本仓库模块一。

---

## 前端对照：你在装什么

| 你要装的 | ≈ 前端熟悉物 | 干什么 |
|----------|--------------|--------|
| **JDK 17** | Node.js LTS | 编译器 + 标准库 + JVM 运行时 |
| **Maven** | npm / pnpm | 依赖、编译、跑主类 |
| **IDEA / VS Code Java** | VS Code + 前端插件 | 跳转、调试、一键 Run |
| `JAVA_HOME` | `nvm` 选中的那份 Node 路径 | 告诉工具「用哪套 JDK」 |

别装成只下载了 **JRE**（只能跑、不能编）。要的是 **JDK**。  
本仓库按 **Java 17** 写（`record`、`List.toList()` 等），**不要用 8**。Spring Boot 3.x 也要求 17+。

---

## 0.1 先摸清本机现状

打开 **新的** PowerShell / 终端：

```powershell
java -version
where.exe java
echo $env:JAVA_HOME
mvn -version
```

常见结果：

| 现象 | 含义 | 怎么办 |
|------|------|--------|
| `java` 不是内部或外部命令 | 没装或没进 PATH | 往下装 JDK |
| `openjdk version "1.8.0_xxx"` | 默认还是 **JDK 8** | 装/切到 17，并修 PATH |
| `17.0.x` | 已经可用 | 跳到 [0.4 Maven](#04-安装-maven) 或直接验证仓库 |
| `mvn` 找不到 | 没装 Maven | 装 3.9+ |
| `mvn -version` 里 Java 仍是 8 | Maven 跟了错的 JDK | 设好 `JAVA_HOME` 后重开终端 |

Windows 上很多人会同时装 8 和 17：`JAVA_HOME` 指向 17，但 `Path` 里 8 的 `bin` 更靠前，于是 `java -version` 仍是 8。下面专门治这个。

---

## 0.2 安装 JDK 17（Windows 推荐）

推荐发行版：**Eclipse Temurin**（Adoptium），免费、稳定、企业常用。Zulu / Microsoft Build of OpenJDK 也行，版本选 **17 (LTS)**。

1. 打开 [https://adoptium.net/](https://adoptium.net/)  
2. Version 选 **17 (LTS)**，OS 选 Windows，Arch 选 x64  
3. 下载 **JDK** 的 `.msi` 安装包并安装  
4. 安装向导里勾选：
   - Set `JAVA_HOME` variable  
   - Add to PATH（若有多版本，装完仍要按下一节核对顺序）

安装后典型路径：

```text
C:\Program Files\Eclipse Adoptium\jdk-17.x.x.x-hotspot\
```

### macOS / Linux（简记）

```bash
# macOS（Homebrew）
brew install --cask temurin@17

# Ubuntu / Debian 示例
sudo apt update
sudo apt install temurin-17-jdk
```

装完同样用 `java -version`、`echo $JAVA_HOME` 核对。

---

## 0.3 配置 JAVA_HOME 与 PATH（Windows）

### 当前用户临时生效（立刻验证用）

路径按你机器上真实的 17 目录改：

```powershell
$env:JAVA_HOME = "C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot"
$env:Path = "$env:JAVA_HOME\bin;" + $env:Path
java -version
# 应看到类似：openjdk version "17.0.21"
```

`Path` 前面加 17 的 `bin`，是为了盖过前面残留的 JDK 8。

### 永久配置（推荐）

1. Win 搜索「环境变量」→ **编辑系统环境变量** → **环境变量**  
2. 系统变量里新建/修改：
   - 变量名：`JAVA_HOME`  
   - 变量值：`C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot`（不要带 `\bin`）  
3. 编辑系统变量 `Path`：
   - 把 `%JAVA_HOME%\bin` 挪到 **靠前**  
   - 若有 `...\jdk-8...\bin`，要么删掉，要么挪到 17 后面  
4. **关掉所有旧终端 / IDE**，再开一个新的 PowerShell，再跑 `java -version`

### 自检清单

```powershell
java -version          # 17.x
javac -version         # 17.x（有 javac 才说明是 JDK 不是裸 JRE）
where.exe java         # 第一条应是 jdk-17 的路径
echo $env:JAVA_HOME    # 指向 jdk-17 目录
```

`where.exe java` 若第一条仍是 `jdk-8`，说明 PATH 顺序还没改对。

---

## 0.4 安装 Maven

Maven ≈ npm：读 `pom.xml`，拉依赖，编译，执行插件。

1. 下载 [Maven Binary zip](https://maven.apache.org/download.cgi)（选 Binary，不要 Source），解压到例如 `C:\dev\apache-maven-3.9.x`  
2. 新建系统变量 `MAVEN_HOME`（或 `M2_HOME`）指向该目录  
3. `Path` 增加 `%MAVEN_HOME%\bin`  
4. 新开终端：

```powershell
mvn -version
```

关注两行：

- `Apache Maven 3.9.x`  
- `Java version: 17.x.x` —— 必须是 17；若仍是 8，回去修 `JAVA_HOME`

国内网络慢时，可在 `%USERPROFILE%\.m2\settings.xml` 配阿里云镜像（没有就新建该文件）：

```xml
<settings>
  <mirrors>
    <mirror>
      <id>aliyun</id>
      <mirrorOf>central</mirrorOf>
      <url>https://maven.aliyun.com/repository/central</url>
    </mirror>
  </mirrors>
</settings>
```

---

## 0.5 IDE：怎么打开本仓库

### IntelliJ IDEA（强烈推荐）

1. 安装 IDEA Community 或 Ultimate  
2. **Open** 本仓库根目录（有父 `pom.xml` 的那层）  
3. 右下角若提示 Trust Project / Load Maven，选信任并加载  
4. `File` → `Project Structure` → **Project SDK** 选 **17**  
5. 打开任意 `*Demo.java`，点 `main` 旁绿色三角 Run

### VS Code

1. 装扩展包 **Extension Pack for Java**（Microsoft）  
2. 打开仓库根目录  
3. `Ctrl+Shift+P` → `Java: Configure Java Runtime`，把 JDK 17 配上  
4. 打开 Demo 文件，右上角 Run

文档站（本手册网页版）另需 Node：

```bash
npm install
npm run docs:dev
# http://localhost:6100
```

跑 Java 示例不依赖文档站。

---

## 0.6 用本仓库验收：编译 + 跑第一个 Demo

在仓库根目录 `Java_For_Frontend_Devs/`：

```powershell
# 确认当前壳子已是 17
java -version

mvn -pl 01-Java-Core-And-OOP -am compile

mvn -pl 01-Java-Core-And-OOP exec:java `
  "-Dexec.mainClass=com.jffd.core.typing.StrongTypingDemo"
```

成功标志：

- `compile` 无 ERROR  
- Demo 往控制台打出几段对比输出（下一章会讲这些输出在说什么）

若编译报错类似 `release version 17 not supported`：当前 `javac` 仍是 8，回到 [0.3](#03-配置-java_home-与-pathwindows)。

---

## 0.7 最小手写 Hello（可选）

不经过 Maven，确认「编译器本身」活着：

```powershell
mkdir $env:TEMP\jffd-hello -Force
Set-Content "$env:TEMP\jffd-hello\Hello.java" @'
public class Hello {
  public static void main(String[] args) {
    System.out.println("hello from java " + System.getProperty("java.version"));
  }
}
'@
Push-Location "$env:TEMP\jffd-hello"
javac Hello.java
java Hello
Pop-Location
```

应打印 `hello from java 17.x.x`。

---

## 避坑

1. **装了 JRE 没装 JDK** → 没有 `javac`，Maven 编译失败  
2. **默认仍是 8** → `JAVA_HOME` 对了但 PATH 里 8 更靠前；用 `where.exe java` 查  
3. **改了环境变量却不重开终端/IDE** → 旧进程仍拿旧 PATH  
4. **公司电脑锁了系统 Path** → 用用户变量 `JAVA_HOME` + 用户 `Path` 前置 17 的 `bin`  
5. **Maven 显示 Java 8、终端 `java` 却是 17** → Maven 读的是 `JAVA_HOME`；把 `JAVA_HOME` 指到 17 后重开终端  
6. **把项目 JDK 设成 8 去硬编本仓库** → 语法过不了，别降级，升运行时

## 面试 / 常识（知道即可）

- JDK / JRE / JVM 各是什么？  
- 为啥现在新项目常直接上 17/21，而不是 8？  
- `JAVA_HOME` 和 `Path` 里的 `java` 不一致时，谁说了算？（命令行看 PATH；多数构建工具看 `JAVA_HOME`）

---

装通了再进语法。下一章 → [01-strong-typing-and-basics.md](./01-strong-typing-and-basics.md)
