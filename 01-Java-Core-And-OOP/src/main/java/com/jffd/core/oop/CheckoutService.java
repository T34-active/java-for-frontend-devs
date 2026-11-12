package com.jffd.core.oop;

import java.util.Objects;

/**
 * 组合优于继承：Checkout「拥有」Payment，而不是 extends Payment。
 * 前端类比：页面组件注入 apiClient，而不是继承 ApiClientPage。
 */
public class CheckoutService {

    private final Payment payment;

    public CheckoutService(Payment payment) {
        this.payment = Objects.requireNonNull(payment, "payment");
    }

    public void checkout(int amountCents) {
        System.out.println("[Checkout] channel=" + payment.channel());
        payment.pay(amountCents);
    }
}
