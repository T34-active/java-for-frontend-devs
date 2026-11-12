package com.jffd.core.oop;

public class SmsNotifier extends AbstractNotifier {

    @Override
    protected String channel() {
        return "SMS";
    }

    @Override
    protected void doSend(String payload) {
        System.out.println("[SmsNotifier] send: " + payload);
    }

    @Override
    protected void afterSend(String userId) {
        System.out.println("[SmsNotifier] audit log for " + userId);
    }
}
