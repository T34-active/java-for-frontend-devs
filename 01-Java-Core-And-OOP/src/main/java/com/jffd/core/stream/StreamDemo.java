package com.jffd.core.stream;

import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

/**
 * 第 5 章示例：Lambda、Stream 管道、分组、惰性短路。
 * 运行：mvn -pl 01-Java-Core-And-OOP exec:java -Dexec.mainClass="com.jffd.core.stream.StreamDemo"
 */
public class StreamDemo {

    record Emp(String name, String dept, int age, int salary) {
    }

    public static void main(String[] args) {
        List<Emp> emps = List.of(
                new Emp("Ada", "FE", 28, 30_000),
                new Emp("Lin", "FE", 22, 18_000),
                new Emp("Bob", "BE", 31, 35_000),
                new Emp("Chen", "BE", 26, 28_000),
                new Emp("Dora", "QA", 24, 16_000)
        );

        mapFilterSort(emps);
        grouping(emps);
        lazyShortCircuit();
        flatMapOptional();
        joiningAndStats(emps);
    }

    /** ≈ users.filter(...).map(...).sort(...) */
    private static void mapFilterSort(List<Emp> emps) {
        List<String> feAdults = emps.stream()
                .filter(e -> "FE".equals(e.dept()))
                .filter(e -> e.age() >= 25)
                .sorted(Comparator.comparingInt(Emp::salary).reversed())
                .map(Emp::name)
                .toList();
        System.out.println("[map/filter/sort] " + feAdults);
    }

    /** ≈ lodash groupBy + countBy */
    private static void grouping(List<Emp> emps) {
        Map<String, Long> countByDept = emps.stream()
                .collect(Collectors.groupingBy(Emp::dept, Collectors.counting()));
        System.out.println("[groupingBy count] " + countByDept);

        Map<String, Integer> salarySum = emps.stream()
                .collect(Collectors.groupingBy(Emp::dept, Collectors.summingInt(Emp::salary)));
        System.out.println("[groupingBy sum] " + salarySum);
    }

    /** 惰性 + 短路：不一定跑完所有元素 */
    private static void lazyShortCircuit() {
        Optional<Integer> firstEvenSquare = List.of(1, 2, 3, 4, 5).stream()
                .peek(n -> System.out.println("  peek filter-in " + n))
                .filter(n -> n % 2 == 0)
                .peek(n -> System.out.println("  peek map-in " + n))
                .map(n -> n * n)
                .findFirst();
        System.out.println("[lazy findFirst] " + firstEvenSquare.orElse(-1));
    }

    /** flatMap 摊平 Optional/集合 ≈ flatMap + compact */
    private static void flatMapOptional() {
        List<Optional<String>> maybeNames = List.of(
                Optional.of("React"),
                Optional.empty(),
                Optional.of("Vue")
        );
        List<String> names = maybeNames.stream()
                .flatMap(Optional::stream) // Java 9+
                .toList();
        System.out.println("[flatMap Optional] " + names);
    }

    private static void joiningAndStats(List<Emp> emps) {
        String csv = emps.stream().map(Emp::name).collect(Collectors.joining(", "));
        System.out.println("[joining] " + csv);

        double avgSalary = emps.stream().mapToInt(Emp::salary).average().orElse(0);
        System.out.println("[average salary] " + avgSalary);

        // Stream 只能消费一次：
        var stream = emps.stream().map(Emp::name);
        System.out.println("[stream once] " + stream.toList());
        // stream.toList(); // 再次终端操作会抛 IllegalStateException
    }
}
