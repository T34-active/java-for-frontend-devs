# 0. 安装 JDK 与工具链

本章说明如何在本机装好 **JDK 17** 和 **Maven**，并用本仓库模块一做一次验收。装通之前，先不要跳进语法章节。

| | |
|--|--|
| 前置 | 会用终端、会装软件；知道「环境变量」大概是什么意思即可。 |
| 学完应能 | 说出 JDK / JRE / JVM 的差别；本机 `java`/`javac`/`mvn` 指向 17；编译并跑通模块一 Demo。 |

下面仍从「要装什么」讲起，按顺序操作，不要跳。

---

## 0.1 你要装的是什么

本仓库需要两样东西：

1. **JDK 17** — Java 开发工具包。里面有编译器 `javac`、运行时 `java`，以及标准库。  
2. **Maven 3.9+** — 读 `pom.xml`、下载依赖、编译、执行主类的构建工具。

注意区分：

- **JDK**：能编译、能运行。本教程要的是这个。  
- **JRE**：通常只能运行已编译程序。只装 JRE，后面 Maven 编译会失败。  
- **JVM**：执行字节码的虚拟机，包含在 JDK 里，一般不用单独装。

本仓库按 **Java 17** 编写（例如 `record`、`List.toList()`）。**不要用 JDK 8**。Spring Boot 3.x 也要求 17+。

若你熟悉前端：JDK 有点像 Node.js 运行时 + 语言工具；Maven 有点像 npm / pnpm。类比只帮记忆，下面仍按 Java 工具本身逐步操作。

---

## 0.2 先查看本机现状

打开一个**新的** PowerShell 或终端，执行：

```powershell
java -version
where.exe java
echo $env:JAVA_HOME
mvn -version
```

对照结果决定下一步：

| 现象 | 含义 | 下一步 |
|------|------|--------|
| `java` 不是内部或外部命令 | 未安装或未进 PATH | 安装 JDK（0.3） |
| `openjdk version "1.8.0_xxx"` | 默认仍是 JDK 8 | 安装/切换到 17，并修 PATH（0.3、0.4） |
| `17.0.x` | Java 已可用 | 检查 Maven（0.5） |
| `mvn` 找不到 | 未装 Maven | 安装 Maven（0.5） |
| `mvn -version` 里 Java 仍是 8 | Maven 跟了错误的 JDK | 设好 `JAVA_HOME` 后重开终端 |

Windows 上常同时装有 8 和 17：`JAVA_HOME` 指向 17，但 `Path` 里 8 的 `bin` 更靠前，于是 `java -version` 仍显示 8。后面专门处理这种情况。

---

## 0.3 安装 JDK 17（Windows）

推荐发行版：**Eclipse Temurin**（Adoptium）。Zulu、Microsoft Build of OpenJDK 也可以，版本选 **17 (LTS)**。

1. 打开 [https://adoptium.net/](https://adoptium.net/)  
2. Version 选 **17 (LTS)**，OS 选 Windows，Arch 选 x64  
3. 下载 **JDK** 的 `.msi` 并安装  
4. 安装向导中勾选：Set `JAVA_HOME` variable；Add to PATH（若本机有多版本，装完仍要按 0.4 核对顺序）

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

## 0.4 配置 `JAVA_HOME` 与 `Path`（Windows）

### 当前终端临时生效（立刻验证）

路径改成你机器上真实的 17 目录：

```powershell
$env:JAVA_HOME = "C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot"
$env:Path = "$env:JAVA_HOME\bin;" + $env:Path
java -version
# 应看到类似：openjdk version "17.0.21"
```

把 17 的 `bin` 放到 `Path` 最前面，是为了盖过残留的 JDK 8。

### 永久配置（推荐）

1. Win 搜索「环境变量」→ **编辑系统环境变量** → **环境变量**  
2. 系统变量中新建或修改：  
   - 变量名：`JAVA_HOME`  
   - 变量值：`C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot`（**不要**带 `\bin`）  
3. 编辑系统变量 `Path`：  
   - 把 `%JAVA_HOME%\bin` 挪到靠前  
   - 若有 `...\jdk-8...\bin`，删除或挪到 17 后面  
4. **关掉所有旧终端和 IDE**，再开新的 PowerShell，再跑 `java -version`

### 自检

```powershell
java -version          # 17.x
javac -version         # 17.x（有 javac 说明是 JDK，不是裸 JRE）
where.exe java         # 第一条应是 jdk-17 的路径
echo $env:JAVA_HOME    # 指向 jdk-17 目录
```

若 `where.exe java` 第一条仍是 `jdk-8`，说明 `Path` 顺序还没改对。

---

## 0.5 安装 Maven

Maven 读取项目根目录的 `pom.xml`，负责依赖下载、编译和插件执行。

1. 下载 [Maven Binary zip](https://maven.apache.org/download.cgi)（选 Binary，不要 Source）  
2. 解压到例如 `C:\dev\apache-maven-3.9.x`  
3. 新建系统变量 `MAVEN_HOME`（或 `M2_HOME`）指向该目录  
4. 在 `Path` 中增加 `%MAVEN_HOME%\bin`  
5. 新开终端：

```powershell
mvn -version
```

关注两行：

- `Apache Maven 3.9.x`  
- `Java version: 17.x.x` —— 必须是 17；若仍是 8，回到 0.4 修 `JAVA_HOME`

国内网络较慢时，可在 `%USERPROFILE%\.m2\settings.xml` 配置镜像（没有该文件就新建）：

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

## 0.6 用 IDE 打开本仓库

### IntelliJ IDEA（推荐）

1. 安装 IDEA Community 或 Ultimate  
2. **Open** 仓库根目录（含父 `pom.xml` 的那一层）  
3. 若提示 Trust Project / Load Maven，选择信任并加载  
4. `File` → `Project Structure` → **Project SDK** 选 **17**  
5. 打开任意 `*Demo.java`，点击 `main` 旁绿色三角运行

### VS Code

1. 安装扩展包 **Extension Pack for Java**（Microsoft）  
2. 打开仓库根目录  
3. `Ctrl+Shift+P` → `Java: Configure Java Runtime`，配置 JDK 17  
4. 打开 Demo 文件，使用右上角 Run

文档站（本手册网页版）另需 Node，与跑 Java 示例无关：

```bash
npm install
npm run docs:dev
# http://localhost:6100
```

---

## 0.7 用本仓库验收

在仓库根目录 `Java_For_Frontend_Devs/`：

```powershell
java -version

mvn -pl 01-Java-Core-And-OOP -am compile

mvn -pl 01-Java-Core-And-OOP exec:java `
  "-Dexec.mainClass=com.jffd.core.typing.StrongTypingDemo"
```

成功标志：

- `compile` 无 ERROR  
- Demo 向控制台打印若干对比输出（下一章会解释这些输出）

若报错类似 `release version 17 not supported`：当前 `javac` 仍是 8，回到 [0.4](#04-配置-java_home-与-pathwindows)。

---

## 0.8 可选：不经过 Maven 的 Hello

确认编译器本身可用：

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

1. 只装了 JRE → 没有 `javac`，Maven 编译失败  
2. 默认仍是 8 → 用 `where.exe java` 查 PATH 顺序  
3. 改了环境变量却不重开终端 / IDE → 旧进程仍用旧 PATH  
4. 系统 Path 被锁定 → 用用户变量 `JAVA_HOME` + 用户 `Path` 前置 17 的 `bin`  
5. 终端 `java` 是 17、Maven 仍报 8 → Maven 读的是 `JAVA_HOME`  
6. 把项目 SDK 降到 8 硬编本仓库 → 语法过不了；升运行时，不要降项目

## 检验一下

对照「学完应能」自问：

1. JDK、JRE、JVM 各是什么？  
2. 为什么本仓库要用 17，而不是 8？  
3. `JAVA_HOME` 与 `Path` 里的 `java` 不一致时，命令行和 Maven 分别看谁？

## 小结

你已经装好（或核对过）JDK 17 与 Maven，并用本仓库完成了一次编译与 Demo 运行。接下来进入语言本身：先认清基本类型与包装类型。

下一章 → [01-strong-typing-and-basics.md](./01-strong-typing-and-basics.md)
