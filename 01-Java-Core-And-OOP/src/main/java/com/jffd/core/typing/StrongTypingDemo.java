package com.jffd.core.typing;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Optional;

/**
 * 第 1 章示例：与 01-strong-typing-and-basics.md 六个知识要点对齐。
 * <p>
 * 运行：mvn -pl 01-Java-Core-And-OOP compile exec:java "-Dexec.mainClass=com.jffd.core.typing.StrongTypingDemo"
 */
public class StrongTypingDemo {

    public static void main(String[] args) {
        walkEachType();
        boxingAndNpe();
        castAndControlFlow();
        equalsVsDoubleEquals();
        finalListAndOverload();
        moneyAndOptional();
    }

    /** 知识要点二：逐个类型走一遍（基本 / 引用 / 包装） */
    private static void walkEachType() {
        // 族 A：基本类型
        int age = 18;
        long userId = 10001L;
        double ratio = 0.1;
        boolean ready = true;
        byte flag = 1;
        short portHint = 8080;
        float score = 98.5f;
        char grade = 'A';
        System.out.println("[primitive] int=" + age + ", long=" + userId
                + ", double=" + ratio + ", boolean=" + ready);
        System.out.println("[primitive] byte=" + flag + ", short=" + portHint
                + ", float=" + score + ", char=" + grade);

        // 族 B：引用类型
        String name = "Ada";
        String noName = null;
        int[] scores = {90, 80, 70};
        List<String> tags = new ArrayList<>();
        tags.add("java");
        System.out.println("[reference] name=" + name + ", noName=" + noName
                + ", scores[0]=" + scores[0] + ", tag=" + tags.get(0));

        // 族 C：包装类型
        Integer boxedInt = age;
        Integer missingInt = null;
        Long boxedLong = userId;
        Double boxedDouble = ratio;
        Boolean boxedFlag = ready;
        System.out.println("[wrapper] Integer=" + boxedInt + ", missing=" + missingInt
                + ", Long=" + boxedLong + ", Double=" + boxedDouble + ", Boolean=" + boxedFlag);
    }

    /** 知识要点二续：装箱 / 拆箱 / Integer 缓存 */
    private static void boxingAndNpe() {
        int raw = 42;
        Integer boxed = raw;
        System.out.println("[boxing] raw=" + raw + ", boxed=" + boxed);

        Integer cachedA = 127;
        Integer cachedB = 127;
        Integer bigA = 128;
        Integer bigB = 128;
        System.out.println("[Integer cache] 127==127 ? " + (cachedA == cachedB));
        System.out.println("[Integer cache] 128==128 ? " + (bigA == bigB));
        System.out.println("[Integer equals] 128.equals(128) ? " + bigA.equals(bigB));

        Integer missing = null;
        // int boom = missing; // 取消注释会 NPE：拆箱
        System.out.println("[NPE demo] missing is null? " + (missing == null));

        List<Integer> userIds = new ArrayList<>();
        userIds.add(1);
        userIds.add(2);
        userIds.add(null);
        System.out.println("[List<Integer>] size=" + userIds.size() + ", third=" + userIds.get(2));
    }

    /** 知识要点三：转换与控制流 */
    private static void castAndControlFlow() {
        double price = 3.14;
        int yuan = (int) price;
        System.out.println("[cast] yuan=" + yuan);

        int a = 7;
        int b = 2;
        System.out.println("[div] intDiv=" + (a / b) + ", realDiv=" + (a / 2.0));

        for (int i = 0; i < 3; i++) {
            System.out.println("[for] i=" + i);
        }
    }

    /** 知识要点四：== 与 equals */
    private static void equalsVsDoubleEquals() {
        String a = new String("hello");
        String b = new String("hello");
        System.out.println("[String] == ? " + (a == b));
        System.out.println("[String] equals ? " + a.equals(b));

        String c = "hello";
        String d = "hello";
        System.out.println("[String pool] c==d ? " + (c == d) + " （别依赖）");

        System.out.println("[Objects.equals] null,null => " + Objects.equals(null, null));
        System.out.println("[role] admin.equals(null) => " + "admin".equals(null));
    }

    /** 知识要点五：final、List、重载、var */
    private static void finalListAndOverload() {
        final List<String> tags = new ArrayList<>();
        tags.add("java");
        System.out.println("[final] tags=" + tags);

        List<String> immutable = List.of("a", "b");
        System.out.println("[List.of] " + immutable);

        print("frontend");
        print(42);

        var title = "inferred";
        System.out.println("[var] title=" + title);
    }

    /** 知识要点六：Optional 与金额 */
    private static void moneyAndOptional() {
        System.out.println("[Optional] " + findUserName(1).orElse("anonymous"));
        System.out.println("[Optional] " + findUserName(99).orElse("anonymous"));

        double bad = 0.1 + 0.2;
        System.out.println("[double] 0.1+0.2 = " + bad);

        BigDecimal ok = new BigDecimal("0.1").add(new BigDecimal("0.2"));
        System.out.println("[BigDecimal] 0.1+0.2 = " + ok);

        BigDecimal pay = new BigDecimal("10.005").setScale(2, RoundingMode.HALF_UP);
        System.out.println("[BigDecimal scale] pay=" + pay);
    }

    private static Optional<String> findUserName(long id) {
        if (id == 1L) {
            return Optional.of("Ada");
        }
        return Optional.empty();
    }

    private static void print(String s) {
        System.out.println("[overload String] " + s);
    }

    private static void print(int n) {
        System.out.println("[overload int] " + n);
    }
}
