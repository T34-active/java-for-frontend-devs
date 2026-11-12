# 6. 异常体系

> 异常决定失败怎么被看见：业务抛什么、边界怎么转成 HTTP、日志怎么留 cause。  
> 对应：[`ExceptionDemo.java`](./src/main/java/com/jffd/core/exception/ExceptionDemo.java)、[`BizException.java`](./src/main/java/com/jffd/core/exception/BizException.java)

---

## 先把前端的错误处理对齐过来

| 前端经验 | Java 对应 |
|----------|-----------|
| `try/catch` | 同名，语义接近 |
| `throw new Error` | `throw`（实际多抛 Exception） |
| Promise rejection / 未捕获 | 线程里未捕获异常（Web 容器有自己的处理） |
| React Error Boundary | Spring `@ControllerAdvice`（模块三） |
| TS 不强制处理失败 | Java 受检异常可强迫你在签名上表态 |

多出来的概念是：受检 vs 非受检。现代业务多数把「业务失败」做成 `RuntimeException` 子类，避免每个方法都 `throws` 到爆炸。

---

## 6.1 继承树

```text
Throwable
├── Error                 OOM、StackOverflow… 一般不 catch
└── Exception
    ├── RuntimeException  非受检：NPE、IAE、业务异常…
    └── IOException 等    受检：必须 catch 或继续 throws
```

| 类型 | 编译器 | 典型例子 | 策略 |
|------|--------|----------|------|
| 受检 Exception | 必须处理 | `IOException`、`SQLException` | 边界转换，或包装成业务异常 |
| RuntimeException | 不强制 | NPE、`BizException` | 业务主流 |
| Error | 别瞎抓 | OOM | 日志/监控，进程可能已不健康 |

企业主流：自定义 `BizException extends RuntimeException`，带 `code` + `message`，在 Controller 层统一变成 JSON。

---

## 6.2 `try/catch/finally` 与 try-with-resources

```java
try {
    doSomething();
} catch (IllegalArgumentException e) {
    log.warn("bad arg", e);   // 把异常对象传进日志，保留栈
} catch (Exception e) {
    log.error("unknown", e);
    throw e;
} finally {
    // 总是执行；关资源优先用下面的语法
}
```

### try-with-resources

≈ C# `using`：离开块自动 `close()`。

```java
try (var reader = Files.newBufferedReader(path, StandardCharsets.UTF_8)) {
    return reader.readLine();
}
```

资源实现 `AutoCloseable` / `Closeable`。流、连接能自动关就别手写 `finally { close() }`，容易漏或掩盖异常。

---

## 6.3 自定义业务异常

```java
public class BizException extends RuntimeException {
    private final int code;

    public BizException(int code, String message) {
        super(message);
        this.code = code;
    }

    public BizException(int code, String message, Throwable cause) {
        super(message, cause); // 保留因果链
        this.code = code;
    }

    public int getCode() { return code; }
}
```

```java
if (amount > balance) {
    throw new BizException(4001, "insufficient balance");
}
```

模块三会变成：

```json
{ "code": 4001, "message": "insufficient balance", "data": null }
```

底层是 SQLException、上层转 BizException 时一定要 `new BizException(..., e)`。不传 cause，排障只看到「业务失败」，丢了根因栈。

---

## 6.4 NPE

TS：

```ts
user?.profile?.city
```

Java 17 日常没有同等普及的语言级可选链，于是：

```java
Integer x = null;
int y = x; // 拆箱 NPE

user.getProfile().getCity();

map.get(k).xxx();

Boolean flag = null;
if (flag) { }
```

防护：

1. 入参：`Objects.requireNonNull(name, "name")`  
2. 少返回 null；单值可用 Optional；集合返回空集合  
3. equals：`"admin".equals(role)` 常量在前  
4. 包装类型先判空再进基本类型运算  
5. Bean Validation（模块三）、IDEA 空分析、SpotBugs  

NPE 不是「初级错误」，是线上 Top 异常之一——靠纪律。

---

## 6.5 生产里怎么用异常

| 做 | 别做 |
|------|------|
| 异常表示意外或业务失败 | 用异常当正常 if/else（慢、难读） |
| `throw new X("...", e)` 保留 cause | catch 后空块 / 只 `printStackTrace` |
| `log.error("ctx...", e)` | 只打 `e.getMessage()` 丢栈 |
| 边界统一转换成响应 | 每层 catch 再包五层无信息包装 |
| 该回滚的异常要穿透出去 | 吞掉异常导致事务误提交 |

别在每个 `setState` 外包 try/catch；在路由边界 / Error Boundary 处理并上报——后端同理。

日志先立标准：

```java
// 好
log.error("withdraw failed, userId={}, amount={}", userId, amount, e);

// 差
e.printStackTrace();
log.error("failed: " + e.getMessage());
```

（SLF4J 在 Spring 模块落地；心智先建立。）

---

## 6.6 事务失效预告（面试高频）

后面 Spring + DB 细讲。现在先埋异常视角：

1. `@Transactional` 被同类自调用 → 走不到代理 → 注解失效  
2. 异常在方法内被 catch 吃掉 → 代理认为没出错 → 不回滚  
3. 默认通常只对 RuntimeException / Error 回滚；受检异常可能要配 `rollbackFor`

这章学的「抛什么、抛不抛得出去」，直接决定账会不会回滚。

---

## 6.7 受检异常在 Lambda 里为啥恶心

函数式接口大多不声明 `throws Exception`：

```java
list.stream().map(path -> Files.readString(path)); // 受检异常编不过
```

常见做法：抽到普通循环、包装成未受检异常、或团队统一的小工具。  
不是你菜，是 Java 历史设计和函数式撞车。

---

## 6.8 先自测

1. 受检 / 非受检差在哪？业务异常为啥常选 RuntimeException？  
2. try-with-resources 为啥优于手写 finally close？  
3. 包装异常不传 cause 有什么后果？  
4. 列出 4 个典型 NPE 场景。  
5. 异常被吞掉为啥会导致事务不回滚？

---

## 6.9 动手

```bash
mvn -pl 01-Java-Core-And-OOP exec:java -Dexec.mainClass="com.jffd.core.exception.ExceptionDemo"
```

对照：受检捕获、业务码 4001、try-with-resources、常量 equals、`requireNonNull`。

---

## 避坑

1. `catch (Exception e) {}`  
2. `printStackTrace` 代替日志  
3. 丢失 cause 的二次包装  
4. 把 Error 当业务异常抓住后继续跑  
5. Stream 里硬抛受检异常把代码写歪  
6. 吞异常导致事务「成功」提交脏数据  

## 面试

- 受检 vs 非受检？  
- `final` / `finally` / `finalize`？（别混）  
- try-with-resources 原理？  
- NPE 常见原因与防范？  
- 事务什么情况下不回滚？  
- 为啥别把异常当控制流？

---

## 模块一收官

跑过第 0 章环境验收 + 六个 Demo 后，你应能：

- [ ] 说清 `==` / `equals`、装箱拆箱与 NPE  
- [ ] 用接口 + 组合表达策略，而不是深继承  
- [ ] 知道 ArrayList/HashMap 复杂度、CME、可变 key  
- [ ] 理解泛型擦除与 PECS  
- [ ] 用 Stream 做 filter/map/groupingBy，知道并行禁区  
- [ ] 设计 `BizException` 并保留 cause  

然后回 [全书路线图](/guide)。准备好了就说「继续模块二」。
