package com.jffd.core.oop;

public class AlipayPayment implements Payment {

    @Override
    public String channel() {
        return "alipay";
    }

    @Override
    public void pay(int amountCents) {
        System.out.println("[Alipay] paid " + amountCents + " cents");
    }
}
