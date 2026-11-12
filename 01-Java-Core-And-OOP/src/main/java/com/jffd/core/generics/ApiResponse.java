package com.jffd.core.generics;

/**
 * 后端统一响应的雏形 —— 模块三会做成全局规范。
 * 前端类比：interface ApiResponse&lt;T&gt; { code; message; data: T }
 */
public class ApiResponse<T> {

    private final int code;
    private final String message;
    private final T data;

    private ApiResponse(int code, String message, T data) {
        this.code = code;
        this.message = message;
        this.data = data;
    }

    public static <T> ApiResponse<T> ok(T data) {
        return new ApiResponse<>(0, "ok", data);
    }

    public static <T> ApiResponse<T> fail(int code, String message) {
        return new ApiResponse<>(code, message, null);
    }

    public int getCode() {
        return code;
    }

    public String getMessage() {
        return message;
    }

    public T getData() {
        return data;
    }

    @Override
    public String toString() {
        return "ApiResponse{code=" + code + ", message='" + message + "', data=" + data + "}";
    }
}
