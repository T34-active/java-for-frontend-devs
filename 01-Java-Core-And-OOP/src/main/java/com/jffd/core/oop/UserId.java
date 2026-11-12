package com.jffd.core.oop;

/**
 * record = 不可变数据载体，自动生成 equals/hashCode/toString/accessor。
 * 前端类比：Readonly<{ value: number }> 且带结构化相等。
 */
public record UserId(long value) {

    public UserId {
        if (value <= 0) {
            throw new IllegalArgumentException("UserId must be positive");
        }
    }
}
