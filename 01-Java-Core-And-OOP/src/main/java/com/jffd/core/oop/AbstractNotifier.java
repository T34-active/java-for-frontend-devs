package com.jffd.core.oop;

/**
 * 模板方法：骨架在父类，差异步骤留给子类。
 * 前端类比：抽象基类组件规定生命周期，子类实现 render 细节。
 */
public abstract class AbstractNotifier {

    /** 对外稳定 API —— 模板方法（不要随便 Override 改流程） */
    public final void notifyUser(String userId, String message) {
        validate(userId, message);
        String payload = format(userId, message);
        doSend(payload);
        afterSend(userId);
    }

    protected void validate(String userId, String message) {
        if (userId == null || userId.isBlank()) {
            throw new IllegalArgumentException("userId required");
        }
        if (message == null || message.isBlank()) {
            throw new IllegalArgumentException("message required");
        }
    }

    protected String format(String userId, String message) {
        return "[" + channel() + "] -> " + userId + ": " + message;
    }

    protected abstract String channel();

    protected abstract void doSend(String payload);

    protected void afterSend(String userId) {
        // 钩子：默认空实现，子类可选覆盖
    }
}
