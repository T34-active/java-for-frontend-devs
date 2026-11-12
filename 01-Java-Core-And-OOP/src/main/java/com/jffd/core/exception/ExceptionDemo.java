package com.jffd.core.exception;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Objects;

/**
 * 第 6 章示例：受检/非受检异常、业务异常、try-with-resources、NPE 防护。
 * 运行：mvn -pl 01-Java-Core-And-OOP exec:java -Dexec.mainClass="com.jffd.core.exception.ExceptionDemo"
 */
public class ExceptionDemo {

    public static void main(String[] args) {
        checkedVsUnchecked();
        bizExceptionFlow();
        tryWithResourcesDemo();
        npeDefense();
    }

    /** 受检异常必须处理；RuntimeException 不强制 */
    private static void checkedVsUnchecked() {
        try {
            mayThrowIo();
        } catch (IOException e) {
            System.out.println("[checked] caught IOException: " + e.getMessage());
        }

        try {
            mayThrowRuntime();
        } catch (IllegalArgumentException e) {
            System.out.println("[unchecked] caught IAE: " + e.getMessage());
        }
    }

    private static void mayThrowIo() throws IOException {
        // 模拟受检异常（不真正碰文件系统失败）
        if (System.currentTimeMillis() > 0) {
            throw new IOException("simulated disk error");
        }
    }

    private static void mayThrowRuntime() {
        throw new IllegalArgumentException("simulated bad arg");
    }

    /** 业务层抛 BizException，边界捕获转「响应」—— 模块三会变成 @ControllerAdvice */
    private static void bizExceptionFlow() {
        try {
            withdraw(100, 50);
            withdraw(30, 50);
        } catch (BizException e) {
            System.out.println("[BizException] code=" + e.getCode() + ", msg=" + e.getMessage());
        }
    }

    private static void withdraw(int balance, int amount) {
        if (amount > balance) {
            throw new BizException(4001, "insufficient balance");
        }
        System.out.println("[withdraw] ok, left=" + (balance - amount));
    }

    /** try-with-resources：离开 try 自动 close，≈ using / 自动释放 */
    private static void tryWithResourcesDemo() {
        try {
            Path temp = Files.createTempFile("jffd-", ".txt");
            try {
                Files.writeString(temp, "hello exception chapter", StandardCharsets.UTF_8);
                try (var reader = Files.newBufferedReader(temp, StandardCharsets.UTF_8)) {
                    System.out.println("[try-with-resources] read: " + reader.readLine());
                }
            } finally {
                Files.deleteIfExists(temp);
            }
        } catch (IOException e) {
            // 保留 cause 再抛是生产常见手法；这里仅演示打印
            throw new BizException(5000, "temp file failed", e);
        }
    }

    private static void npeDefense() {
        String input = null;
        // ✅ 常量在前，避免 input.equals 时 NPE
        if ("admin".equals(input)) {
            System.out.println("admin");
        } else {
            System.out.println("[NPE defense] constant-first equals ok");
        }

        try {
            requireName(null);
        } catch (NullPointerException e) {
            System.out.println("[requireNonNull] " + e.getMessage());
        }
    }

    private static void requireName(String name) {
        Objects.requireNonNull(name, "name must not be null");
    }
}
