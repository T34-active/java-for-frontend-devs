package com.jffd.core.oop;

public class WechatPayment implements Payment {

    @Override
    public String channel() {
        return "wechat";
    }

    @Override
    public void pay(int amountCents) {
        System.out.println("[Wechat] paid " + amountCents + " cents");
    }
}
