package com.jffd.core.exception;

/**
 * 业务异常：继承 RuntimeException，避免污染方法签名。
 * 前端类比：带 code 的业务错误对象，最终会被边界层（Controller）转成 JSON。
 */
public class BizException extends RuntimeException {

    private final int code;

    public BizException(int code, String message) {
        super(message);
        this.code = code;
    }

    public BizException(int code, String message, Throwable cause) {
        super(message, cause);
        this.code = code;
    }

    public int getCode() {
        return code;
    }
}
