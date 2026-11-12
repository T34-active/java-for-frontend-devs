package com.jffd.core.oop;

/**
 * 支付能力契约 —— 前端类比：必须实现的 Protocol / 策略接口。
 */
public interface Payment {

    /** @return 支付渠道名，便于日志 */
    String channel();

    /** 支付金额（演示用 int；生产金额请用 BigDecimal） */
    void pay(int amountCents);
}
