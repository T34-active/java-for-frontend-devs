package com.jffd.core.collections;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;

/**
 * 第 3 章示例：List/Map/Set 常用 API、fail-fast、LinkedHashMap 插入序。
 * 运行：mvn -pl 01-Java-Core-And-OOP exec:java -Dexec.mainClass="com.jffd.core.collections.CollectionsDemo"
 */
public class CollectionsDemo {

    public static void main(String[] args) {
        arrayListBasics();
        hashMapBasics();
        failFastVsRemoveIf();
        linkedHashMapOrder();
        setDedup();
        mutableKeyTrap();
    }

    private static void arrayListBasics() {
        List<String> frameworks = new ArrayList<>(4);
        frameworks.add("React");
        frameworks.add("Vue");
        frameworks.add(1, "Svelte"); // 中间插入会搬移元素 O(n)
        System.out.println("[ArrayList] " + frameworks);
        System.out.println("[ArrayList get] " + frameworks.get(0));
    }

    private static void hashMapBasics() {
        Map<String, Integer> stars = new HashMap<>();
        stars.put("react", 220_000);
        stars.put("vue", 210_000);
        stars.putIfAbsent("vue", 1); // 已存在则不覆盖

        System.out.println("[HashMap getOrDefault] angular=" + stars.getOrDefault("angular", 0));
        stars.forEach((k, v) -> System.out.println("[HashMap] " + k + " -> " + v));
    }

    /** foreach 中结构性修改会 CME；用 removeIf */
    private static void failFastVsRemoveIf() {
        List<String> list = new ArrayList<>(List.of("a", "b", "c", "b"));
        // 错误示范（不要打开）：
        // for (String s : list) { if (s.equals("b")) list.remove(s); }

        list.removeIf(s -> s.equals("b"));
        System.out.println("[removeIf] " + list);
    }

    private static void linkedHashMapOrder() {
        Map<String, String> ordered = new LinkedHashMap<>();
        ordered.put("first", "1");
        ordered.put("second", "2");
        ordered.put("third", "3");
        System.out.println("[LinkedHashMap insertion order] " + ordered.keySet());
    }

    private static void setDedup() {
        Set<String> tags = new HashSet<>();
        tags.add("java");
        tags.add("java");
        tags.add("ts");
        System.out.println("[HashSet] " + tags + ", size=" + tags.size());
    }

    /**
     * 可变 key 陷阱：equals/hashCode 依赖的字段被修改后，HashMap 找不到条目。
     * 前端类比：用对象当 Map key 且改了对象内容。
     */
    private static void mutableKeyTrap() {
        Map<MutableKey, String> map = new HashMap<>();
        MutableKey key = new MutableKey("before");
        map.put(key, "value");
        System.out.println("[mutable key] before change get=" + map.get(key));

        key.setName("after"); // 破坏哈希定位
        System.out.println("[mutable key] after change get=" + map.get(key)); // 往往是 null
        System.out.println("[mutable key] containsValue? " + map.containsValue("value"));
    }

    /** 演示用：故意可变的 key —— 生产中 key 应不可变 */
    static final class MutableKey {
        private String name;

        MutableKey(String name) {
            this.name = name;
        }

        void setName(String name) {
            this.name = name;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (!(o instanceof MutableKey that)) {
                return false;
            }
            return Objects.equals(name, that.name);
        }

        @Override
        public int hashCode() {
            return Objects.hash(name);
        }
    }
}
