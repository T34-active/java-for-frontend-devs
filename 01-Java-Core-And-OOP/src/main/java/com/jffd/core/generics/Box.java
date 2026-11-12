package com.jffd.core.generics;

/**
 * 最简单的泛型容器 ≈ TS: type Box&lt;T&gt; = { value: T }
 */
public class Box<T> {

    private T value;

    public void set(T value) {
        this.value = value;
    }

    public T get() {
        return value;
    }

    @Override
    public String toString() {
        return "Box(" + value + ")";
    }
}
