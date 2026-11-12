package com.jffd.core.typing;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Optional;

/**
 * 第 1 章示例：强类型、装箱、==/equals、final、Optional。
 * <p>
 * 前端类比：TS strict 模式 + 运行时也不帮你隐式转换。
 * 运行：mvn -pl 01-Java-Core-And-OOP exec:java -Dexec.mainClass="com.jffd.core.typing.StrongTypingDemo"
 */
public class StrongTypingDemo {

    public static void main(String[] args) {
        boxingAndNpe();
        equalsVsDoubleEquals();
        finalIsShallow();
        moneyMustUseBigDecimal();
        optionalStyle();
        overloadAndVar();
    }

    /** 装箱 / 拆箱 —— Integer 可为 null，拆箱时 NPE */
    private static void boxingAndNpe() {
        int primitive = 42;
        Integer boxed = primitive; // 自动装箱 ≈ 把 number 包成 Number 对象
        System.out.println("[boxing] primitive=" + primitive + ", boxed=" + boxed);

        Integer cachedA = 127;
        Integer cachedB = 127;
        Integer bigA = 128;
        Integer bigB = 128;
        // [-128, 127] 有缓存，== 可能为 true；超出则 false —— 业务禁止用 == 比 Integer
        System.out.println("[Integer cache] 127==127 ? " + (cachedA == cachedB));
        System.out.println("[Integer cache] 128==128 ? " + (bigA == bigB));
        System.out.println("[Integer equals] 128.equals(128) ? " + bigA.equals(bigB));

        Integer oops = null;
        // 取消下一行注释会 NPE：拆箱成 int 时读取 null
        // int exploded = oops;
        System.out.println("[NPE demo] oops is null, skip unboxing. value=" + oops);
    }

    /** == 比引用；equals 比内容。String 常量池别当成特性依赖 */
    private static void equalsVsDoubleEquals() {
        String a = new String("hello");
        String b = new String("hello");
        System.out.println("[String] a==b ? " + (a == b));
        System.out.println("[String] a.equals(b) ? " + a.equals(b));

        String c = "hello";
        String d = "hello";
        System.out.println("[String pool] c==d ? " + (c == d) + " （别依赖）");

        // null 安全比较 ≈ TS 里 (a === b) 但对 null 友好
        System.out.println("[Objects.equals] null,null => " + Objects.equals(null, null));
    }

    /** final ≈ const：锁引用，不锁内容 */
    private static void finalIsShallow() {
        final List<String> list = new ArrayList<>();
        list.add("react");
        list.add("vue");
        // list = new ArrayList<>(); // 编译错误
        System.out.println("[final] list content mutable: " + list);

        // 真正不可变列表（Java 9+）
        List<String> immutable = List.of("a", "b");
        System.out.println("[List.of] " + immutable);
        // immutable.add("c"); // UnsupportedOperationException
    }

    /** 金额禁忌 double —— 前端若用 number 算钱同样会漂 */
    private static void moneyMustUseBigDecimal() {
        double bad = 0.1 + 0.2;
        System.out.println("[double] 0.1+0.2 = " + bad); // 0.30000000000000004

        BigDecimal ok = new BigDecimal("0.1").add(new BigDecimal("0.2"));
        System.out.println("[BigDecimal] 0.1+0.2 = " + ok);

        BigDecimal price = new BigDecimal("10.005");
        BigDecimal rounded = price.setScale(2, RoundingMode.HALF_UP);
        System.out.println("[BigDecimal scale] " + price + " -> " + rounded);
    }

    /** Optional 用于返回值「可能没有」，不要当到处传的字段类型 */
    private static void optionalStyle() {
        System.out.println("[Optional] " + findUserName(1).orElse("anonymous"));
        System.out.println("[Optional] " + findUserName(99).orElse("anonymous"));

        findUserName(1).ifPresent(name -> System.out.println("[Optional ifPresent] hi, " + name));
    }

    private static Optional<String> findUserName(long id) {
        if (id == 1L) {
            return Optional.of("Ada");
        }
        return Optional.empty(); // 不要 return null
    }

    /** 重载 + 局部 var */
    private static void overloadAndVar() {
        print("frontend");
        print(42);
        var inferred = "type inferred locally";
        System.out.println("[var] " + inferred);
    }

    private static void print(String s) {
        System.out.println("[overload String] " + s);
    }

    private static void print(int n) {
        System.out.println("[overload int] " + n);
    }
}
