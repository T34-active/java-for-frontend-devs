package com.jffd.core.generics;

import java.util.ArrayList;
import java.util.List;

/**
 * 第 4 章示例：泛型类/方法、PECS、擦除限制的绕法。
 * 运行：mvn -pl 01-Java-Core-And-OOP exec:java -Dexec.mainClass="com.jffd.core.generics.GenericsDemo"
 */
public class GenericsDemo {

    public static void main(String[] args) throws Exception {
        genericBoxAndResponse();
        genericMethod();
        pecsDemo();
        classTokenWorkaround();
    }

    private static void genericBoxAndResponse() {
        Box<String> box = new Box<>();
        box.set("hello generics");
        System.out.println("[Box] " + box);

        ApiResponse<Box<String>> resp = ApiResponse.ok(box);
        System.out.println("[ApiResponse] " + resp);
    }

    private static void genericMethod() {
        System.out.println("[first] " + first(List.of("a", "b", "c")));
        System.out.println("[max] " + max("vue", "react"));
    }

    private static <T> T first(List<T> list) {
        return list.isEmpty() ? null : list.get(0);
    }

    private static <T extends Comparable<T>> T max(T a, T b) {
        return a.compareTo(b) >= 0 ? a : b;
    }

    /** PECS：Producer Extends, Consumer Super */
    private static void pecsDemo() {
        List<Integer> integers = List.of(1, 2, 3);
        List<Double> doubles = List.of(1.5, 2.5);
        System.out.println("[sum extends] ints=" + sum(integers) + ", doubles=" + sum(doubles));

        List<Number> numbers = new ArrayList<>();
        fillIntegers(numbers);
        System.out.println("[super consumer] " + numbers);
    }

    private static double sum(List<? extends Number> source) {
        double total = 0;
        for (Number n : source) {
            total += n.doubleValue();
        }
        // source.add(1); // 编译错误：不知道具体是 Integer 还是 Double
        return total;
    }

    private static void fillIntegers(List<? super Integer> sink) {
        sink.add(10);
        sink.add(20);
        // Integer x = sink.get(0); // 编译错误：取出只能当 Object
    }

    /**
     * 擦除后不能 new T()，把 Class&lt;T&gt; 当「运行时类型令牌」传入。
     * 前端类比：zod schema / class constructor 传入以保留运行时信息。
     */
    private static void classTokenWorkaround() throws Exception {
        String created = create(String.class);
        System.out.println("[Class<T> token] created empty String length=" + created.length());
    }

    private static <T> T create(Class<T> type) throws Exception {
        return type.getDeclaredConstructor().newInstance();
    }
}
