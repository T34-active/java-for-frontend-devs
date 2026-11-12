package com.jffd.core.oop;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * 第 2 章示例：接口多态、模板方法、组合、equals/hashCode、record。
 * 运行：mvn -pl 01-Java-Core-And-OOP exec:java -Dexec.mainClass="com.jffd.core.oop.OopDemo"
 */
public class OopDemo {

    public static void main(String[] args) {
        polymorphismAndStrategy();
        templateMethod();
        compositionOverInheritance();
        equalsHashCodeContract();
        recordValueObject();
    }

    /** 编译期类型是 Payment，运行期走具体实现 —— 策略模式基础 */
    private static void polymorphismAndStrategy() {
        List<Payment> payments = List.of(new AlipayPayment(), new WechatPayment());
        for (Payment payment : payments) {
            payment.pay(1999);
        }
    }

    /** 抽象类固定流程，子类填差异步骤 */
    private static void templateMethod() {
        AbstractNotifier notifier = new SmsNotifier();
        notifier.notifyUser("u-100", "Your order has shipped");
    }

    /** 组合：替换 Payment 实现即可换渠道，无需改 CheckoutService */
    private static void compositionOverInheritance() {
        CheckoutService alipayCheckout = new CheckoutService(new AlipayPayment());
        alipayCheckout.checkout(5000);

        CheckoutService wechatCheckout = new CheckoutService(new WechatPayment());
        wechatCheckout.checkout(5000);
    }

    /** equals 相等 => hashCode 必须相等；HashSet 去重靠这套契约 */
    private static void equalsHashCodeContract() {
        User a = new User(1L, "a@example.com");
        User b = new User(1L, "b@example.com"); // 同 id，业务 equals 视为同一用户
        System.out.println("[equals] a.equals(b) ? " + a.equals(b));
        System.out.println("[hashCode] same? " + (a.hashCode() == b.hashCode()));

        Set<User> set = new HashSet<>();
        set.add(a);
        set.add(b);
        System.out.println("[HashSet size] expect 1, actual=" + set.size());
    }

    private static void recordValueObject() {
        UserId id1 = new UserId(10);
        UserId id2 = new UserId(10);
        System.out.println("[record] id1=" + id1 + ", equals? " + id1.equals(id2));
        // new UserId(0); // 紧凑构造器会拒绝
    }
}
