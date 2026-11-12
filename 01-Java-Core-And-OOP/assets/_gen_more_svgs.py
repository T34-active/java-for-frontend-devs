# -*- coding: utf-8 -*-
"""Generate remaining mental-model SVGs for module 1 chapters."""
from pathlib import Path

root = Path(__file__).resolve().parent

STYLE = """
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#334155"/>
    </marker>
    <marker id="arrow-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#0f766e"/>
    </marker>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#1d4ed8"/>
    </marker>
    <marker id="arrow-rose" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#be123c"/>
    </marker>
    <style><![CDATA[
      .title { font: 700 15px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #0f172a; }
      .sub { font: 600 12px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #64748b; }
      .node-text { font: 600 13px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #0f172a; }
      .code { font: 600 12px ui-monospace, Consolas, monospace; fill: #334155; }
      .ok { font: 600 12px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #047857; }
      .bad { font: 600 12px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #be123c; }
      .panel { fill: #f8fafc; stroke: #e2e8f0; stroke-width: 1.5; }
      .box { fill: #f8fafc; stroke: #64748b; stroke-width: 2; }
      .box-teal { fill: #ecfdf5; stroke: #0f766e; stroke-width: 2; }
      .box-orange { fill: #fff7ed; stroke: #c2410c; stroke-width: 2; }
      .box-blue { fill: #eff6ff; stroke: #2563eb; stroke-width: 2; }
      .box-rose { fill: #fff1f2; stroke: #e11d48; stroke-width: 2; }
      .box-amber { fill: #fffbeb; stroke: #d97706; stroke-width: 2; }
    ]]></style>
  </defs>
"""

files = {}

files["cast-and-control-flow.svg"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 460" role="img">
  <title>类型转换与控制流</title>
  {STYLE}
  <text class="title" x="24" y="28">类型转换与控制流</text>

  <rect class="panel" x="16" y="44" width="728" height="120" rx="10"/>
  <text class="title" x="36" y="70">拓宽（自动）</text>
  <rect class="box-teal" x="40" y="88" width="70" height="44" rx="8"/><text class="node-text" x="60" y="116">int</text>
  <line x1="110" y1="110" x2="150" y2="110" stroke="#0f766e" stroke-width="2" marker-end="url(#arrow-teal)"/>
  <rect class="box-teal" x="150" y="88" width="70" height="44" rx="8"/><text class="node-text" x="165" y="116">long</text>
  <line x1="220" y1="110" x2="260" y2="110" stroke="#0f766e" stroke-width="2" marker-end="url(#arrow-teal)"/>
  <rect class="box-teal" x="260" y="88" width="80" height="44" rx="8"/><text class="node-text" x="272" y="116">double</text>
  <text class="sub" x="360" y="116">信息容量够 → 编译器自动做</text>

  <rect class="panel" x="16" y="180" width="728" height="100" rx="10"/>
  <text class="title" x="36" y="206">收窄（必须强制转换）</text>
  <text class="code" x="36" y="236">double 3.14 ──(int)──► int 3　（小数直接丢弃）</text>
  <text class="code" x="36" y="260">"42" ──parseInt──► 42　　42 ──valueOf──► "42"</text>

  <rect class="panel" x="16" y="296" width="350" height="140" rx="10"/>
  <text class="title" x="36" y="322">if 条件</text>
  <rect class="box" x="90" y="340" width="180" height="36" rx="6"/><text class="node-text" x="115" y="363">条件必须 boolean</text>
  <line x1="140" y1="376" x2="100" y2="410" stroke="#047857" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="220" y1="376" x2="260" y2="410" stroke="#be123c" stroke-width="2" marker-end="url(#arrow-rose)"/>
  <text class="ok" x="60" y="428">true → 进入块</text>
  <text class="bad" x="210" y="428">false → else</text>

  <rect class="panel" x="384" y="296" width="360" height="140" rx="10"/>
  <text class="title" x="404" y="322">for 循环</text>
  <text class="code" x="404" y="352">初始化 → 条件? → 执行体 → 步进 → …</text>
  <text class="sub" x="404" y="382">条件为 true 才继续；增强 for：逐个取出元素</text>
</svg>
"""

files["equals-reference.svg"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 420" role="img">
  <title>== 比引用，equals 比内容</title>
  {STYLE}
  <text class="title" x="24" y="28">== 比引用 · equals 比内容</text>

  <rect class="panel" x="16" y="48" width="728" height="200" rx="10"/>
  <text class="code" x="36" y="76">String a = new String("hello");  String b = new String("hello");</text>
  <rect class="box-teal" x="60" y="100" width="50" height="36" rx="6"/><text class="node-text" x="76" y="123">a</text>
  <line x1="110" y1="118" x2="180" y2="118" stroke="#0f766e" stroke-width="2" marker-end="url(#arrow-teal)"/>
  <rect class="box-orange" x="180" y="92" width="160" height="52" rx="8"/><text class="node-text" x="200" y="124">"hello" 对象 #1</text>

  <rect class="box-teal" x="60" y="170" width="50" height="36" rx="6"/><text class="node-text" x="76" y="193">b</text>
  <line x1="110" y1="188" x2="180" y2="188" stroke="#0f766e" stroke-width="2" marker-end="url(#arrow-teal)"/>
  <rect class="box-orange" x="180" y="162" width="160" height="52" rx="8"/><text class="node-text" x="200" y="194">"hello" 对象 #2</text>

  <text class="bad" x="400" y="130">a == b → false（箭头不同）</text>
  <text class="ok" x="400" y="170">a.equals(b) → true（字符相同）</text>

  <rect class="panel" x="16" y="268" width="728" height="130" rx="10"/>
  <text class="code" x="36" y="296">String c = "hello";  String d = "hello";</text>
  <text class="sub" x="36" y="328">字面量常进常量池，c 与 d 可能指向同一对象 → c == d 常为 true</text>
  <text class="bad" x="36" y="360">这是优化，不是业务特性 —— 禁止依赖 == 比字符串</text>
</svg>
"""

files["final-list-array.svg"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img">
  <title>final 锁绑定；数组定长；List 可变长</title>
  {STYLE}
  <text class="title" x="24" y="28">final · 数组 · List</text>

  <rect class="panel" x="16" y="48" width="728" height="150" rx="10"/>
  <text class="code" x="36" y="76">final List&lt;String&gt; list = new ArrayList&lt;&gt;();</text>
  <rect class="box-teal" x="40" y="100" width="90" height="60" rx="8"/><text class="node-text" x="58" y="136">list</text>
  <line x1="130" y1="130" x2="220" y2="130" stroke="#0f766e" stroke-width="2.5" marker-end="url(#arrow-teal)"/>
  <text class="sub" x="145" y="118">冻结绑定</text>
  <rect class="box-orange" x="220" y="96" width="200" height="68" rx="8"/>
  <text class="node-text" x="245" y="126">ArrayList 对象</text>
  <text class="ok" x="450" y="120">list.add("x") ✅ 改内容</text>
  <text class="bad" x="450" y="150">list = 别的列表 ❌</text>

  <rect class="panel" x="16" y="218" width="350" height="120" rx="10"/>
  <text class="title" x="36" y="246">数组 T[]</text>
  <text class="code" x="36" y="276">{"a","b"} 长度创建时固定</text>
  <text class="sub" x="36" y="306">用 .length 字段</text>

  <rect class="panel" x="384" y="218" width="360" height="120" rx="10"/>
  <text class="title" x="404" y="246">List</text>
  <text class="code" x="404" y="276">add / remove 改变长度</text>
  <text class="sub" x="404" y="306">用 .size() 方法</text>
</svg>
"""

files["null-optional-string.svg"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 420" role="img">
  <title>NPE、Optional 与 String 不可变</title>
  {STYLE}
  <text class="title" x="24" y="28">空引用 · Optional · String 不可变</text>

  <rect class="panel" x="16" y="48" width="240" height="160" rx="10"/>
  <text class="title" x="36" y="76">NPE</text>
  <text class="code" x="36" y="104">user = null</text>
  <text class="code" x="36" y="128">user.getName()</text>
  <line x1="120" y1="140" x2="120" y2="168" stroke="#be123c" stroke-width="2" marker-end="url(#arrow-rose)"/>
  <text class="bad" x="40" y="188">无法分发 → NPE</text>

  <rect class="panel" x="272" y="48" width="280" height="160" rx="10"/>
  <text class="title" x="292" y="76">Optional</text>
  <rect class="box-blue" x="300" y="96" width="100" height="40" rx="6"/><text class="node-text" x="318" y="122">有值盒子</text>
  <rect class="box" x="420" y="96" width="100" height="40" rx="6"/><text class="node-text" x="440" y="122">empty</text>
  <text class="sub" x="300" y="168">orElse / orElseThrow / ifPresent</text>

  <rect class="panel" x="568" y="48" width="176" height="160" rx="10"/>
  <text class="title" x="584" y="76">String</text>
  <text class="code" x="584" y="110">s = "Ada"</text>
  <text class="code" x="584" y="136">toUpperCase()</text>
  <text class="ok" x="584" y="170">新 "ADA"</text>
  <text class="sub" x="584" y="192">原 s 仍 Ada</text>

  <rect class="panel" x="16" y="232" width="728" height="160" rx="10"/>
  <text class="title" x="36" y="262">金额用 BigDecimal，不用 double</text>
  <text class="bad" x="36" y="300">0.1 + 0.2 (double) → 0.30000000000000004</text>
  <text class="ok" x="36" y="336">new BigDecimal("0.1").add(new BigDecimal("0.2")) → 0.3</text>
  <text class="sub" x="36" y="368">用字符串构造，避免 double 误差被固化进 BigDecimal</text>
</svg>
"""

# Chapter 2
files["composition-vs-inheritance.svg"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img">
  <title>继承、组合与接口</title>
  {STYLE}
  <text class="title" x="24" y="28">三种关系：is-a · has-a · can-do</text>

  <rect class="panel" x="16" y="48" width="230" height="260" rx="10"/>
  <text class="title" x="36" y="78">extends 继承</text>
  <text class="sub" x="36" y="104">A 是一种 B（is-a）</text>
  <rect class="box" x="50" y="130" width="150" height="40" rx="6"/><text class="node-text" x="95" y="156">父类 B</text>
  <line x1="125" y1="170" x2="125" y2="198" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>
  <rect class="box-teal" x="50" y="200" width="150" height="40" rx="6"/><text class="node-text" x="95" y="226">子类 A</text>
  <text class="sub" x="36" y="270">只能单继承</text>

  <rect class="panel" x="262" y="48" width="230" height="260" rx="10"/>
  <text class="title" x="282" y="78">组合 has-a</text>
  <text class="sub" x="282" y="104">A 拥有一个 B</text>
  <rect class="box-teal" x="296" y="130" width="160" height="50" rx="6"/><text class="node-text" x="310" y="162">CheckoutService</text>
  <line x1="376" y1="180" x2="376" y2="208" stroke="#0f766e" stroke-width="2" marker-end="url(#arrow-teal)"/>
  <rect class="box-orange" x="296" y="210" width="160" height="40" rx="6"/><text class="node-text" x="330" y="236">Payment</text>
  <text class="sub" x="282" y="280">优先复用行为</text>

  <rect class="panel" x="508" y="48" width="236" height="260" rx="10"/>
  <text class="title" x="528" y="78">implements</text>
  <text class="sub" x="528" y="104">A 具备能力（can-do）</text>
  <rect class="box-blue" x="540" y="130" width="170" height="40" rx="6"/><text class="node-text" x="575" y="156">interface Payment</text>
  <line x1="625" y1="170" x2="625" y2="198" stroke="#1d4ed8" stroke-width="2" marker-end="url(#arrow-blue)"/>
  <rect class="box-teal" x="540" y="200" width="170" height="40" rx="6"/><text class="node-text" x="560" y="226">AlipayPayment</text>
  <text class="sub" x="528" y="280">可实现多个接口</text>
</svg>
"""

files["polymorphism-dispatch.svg"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 300" role="img">
  <title>多态：按实际对象类型分发</title>
  {STYLE}
  <text class="title" x="24" y="28">多态：编译期看声明类型，运行期看真实对象</text>

  <text class="code" x="36" y="64">Payment p = new AlipayPayment();  p.pay(100);</text>

  <rect class="box-teal" x="60" y="90" width="70" height="44" rx="8"/><text class="node-text" x="82" y="118">p</text>
  <line x1="130" y1="112" x2="220" y2="112" stroke="#0f766e" stroke-width="2.5" marker-end="url(#arrow-teal)"/>
  <rect class="box-orange" x="220" y="80" width="200" height="64" rx="8"/>
  <text class="node-text" x="240" y="110">AlipayPayment 对象</text>
  <text class="sub" x="240" y="132">真实类型</text>

  <line x1="420" y1="112" x2="500" y2="112" stroke="#1d4ed8" stroke-width="2" marker-end="url(#arrow-blue)"/>
  <rect class="box-blue" x="500" y="80" width="220" height="64" rx="8"/>
  <text class="node-text" x="520" y="110">调用 Alipay 的 pay</text>
  <text class="sub" x="520" y="132">不是父类空实现</text>

  <text class="sub" x="36" y="200">声明类型 Payment 决定「能调用哪些方法」；运行时对象类型决定「跑哪份实现」。</text>
  <text class="sub" x="36" y="232">这就是接口 + 组合能在 Spring 里替换实现的基础。</text>
</svg>
"""

# Chapter 3
files["collection-hierarchy.svg"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 400" role="img">
  <title>集合接口族谱</title>
  {STYLE}
  <text class="title" x="24" y="28">Java 集合接口族谱</text>

  <rect class="box" x="280" y="52" width="160" height="40" rx="8"/><text class="node-text" x="325" y="78">Iterable</text>
  <line x1="360" y1="92" x2="360" y2="118" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>
  <rect class="box-blue" x="260" y="120" width="200" height="40" rx="8"/><text class="node-text" x="310" y="146">Collection</text>

  <line x1="360" y1="160" x2="140" y2="200" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="360" y1="160" x2="360" y2="200" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="360" y1="160" x2="580" y2="200" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>

  <rect class="box-teal" x="50" y="204" width="180" height="70" rx="8"/>
  <text class="node-text" x="115" y="234">List</text>
  <text class="sub" x="70" y="258">有序·可下标·可重复</text>

  <rect class="box-teal" x="260" y="204" width="200" height="70" rx="8"/>
  <text class="node-text" x="335" y="234">Set</text>
  <text class="sub" x="290" y="258">不重复（序看实现）</text>

  <rect class="box-teal" x="490" y="204" width="200" height="70" rx="8"/>
  <text class="node-text" x="555" y="234">Queue</text>
  <text class="sub" x="520" y="258">排队 / 双端等</text>

  <rect class="box-orange" x="260" y="310" width="200" height="60" rx="8"/>
  <text class="node-text" x="330" y="338">Map</text>
  <text class="sub" x="290" y="358">键值映射·独立体系</text>
  <text class="sub" x="480" y="345">不是 Collection 子接口</text>
</svg>
"""

files["arraylist-structure.svg"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 240" role="img">
  <title>ArrayList 底层结构</title>
  {STYLE}
  <text class="title" x="24" y="28">ArrayList ≈ 可扩容数组</text>
  <text class="code" x="24" y="56">Object[] elementData　+　int size</text>

  <rect class="box-blue" x="40" y="90" width="80" height="60" rx="6"/><text class="node-text" x="58" y="126">"a"</text>
  <rect class="box-blue" x="130" y="90" width="80" height="60" rx="6"/><text class="node-text" x="148" y="126">"b"</text>
  <rect class="box-blue" x="220" y="90" width="80" height="60" rx="6"/><text class="node-text" x="238" y="126">"c"</text>
  <rect class="box" x="310" y="90" width="80" height="60" rx="6"/><text class="sub" x="330" y="126">空槽</text>
  <rect class="box" x="400" y="90" width="80" height="60" rx="6"/><text class="sub" x="420" y="126">空槽</text>

  <text class="ok" x="40" y="190">尾部 add 摊还 O(1)；中间插入/删除要搬移 → O(n)；get(i) 为 O(1)</text>
</svg>
"""

files["hashmap-buckets.svg"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img">
  <title>HashMap 桶与查找</title>
  {STYLE}
  <text class="title" x="24" y="28">HashMap：hash → 桶 → equals</text>

  <text class="code" x="36" y="60">Node&lt;K,V&gt;[] table</text>

  <rect class="box" x="40" y="90" width="70" height="40" rx="6"/><text class="node-text" x="58" y="116">桶0</text>
  <rect class="box-blue" x="40" y="150" width="70" height="40" rx="6"/><text class="node-text" x="58" y="176">桶1</text>
  <rect class="box" x="40" y="210" width="70" height="40" rx="6"/><text class="node-text" x="58" y="236">桶2</text>
  <rect class="box-amber" x="40" y="270" width="70" height="40" rx="6"/><text class="node-text" x="58" y="296">桶3</text>

  <line x1="110" y1="170" x2="180" y2="170" stroke="#1d4ed8" stroke-width="2" marker-end="url(#arrow-blue)"/>
  <rect class="box-teal" x="180" y="150" width="120" height="40" rx="6"/><text class="node-text" x="200" y="176">k1=v1</text>
  <line x1="300" y1="170" x2="360" y2="170" stroke="#1d4ed8" stroke-width="2" marker-end="url(#arrow-blue)"/>
  <rect class="box-teal" x="360" y="150" width="120" height="40" rx="6"/><text class="node-text" x="380" y="176">k2=v2</text>
  <text class="sub" x="500" y="176">链表（过长可能树化）</text>

  <text class="sub" x="180" y="240">放入/查找：算 hash → 落到桶 → 桶内 equals 比键</text>
  <text class="sub" x="180" y="270">元素过多超过负载阈值时扩容；键的 hashCode/equals 必须正确且稳定</text>
</svg>
"""

files["mutable-key-pitfall.svg"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 280" role="img">
  <title>可变键导致 HashMap 丢失</title>
  {STYLE}
  <text class="title" x="24" y="28">可变 key 的典型事故</text>

  <rect class="box" x="40" y="60" width="160" height="48" rx="8"/><text class="node-text" x="55" y="90">1. put 可变 key</text>
  <line x1="200" y1="84" x2="250" y2="84" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>
  <rect class="box-amber" x="250" y="60" width="200" height="48" rx="8"/><text class="node-text" x="270" y="90">2. 改 hash 相关字段</text>
  <line x1="450" y1="84" x2="500" y2="84" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>
  <rect class="box-rose" x="500" y="60" width="200" height="48" rx="8"/><text class="node-text" x="520" y="90">3. get → null</text>

  <text class="bad" x="40" y="160">再 get 时算到别的桶；旧 entry 其实还在（containsValue 可能仍 true）</text>
  <text class="ok" x="40" y="200">键优先：String / Long / record / 枚举等不可变类型</text>
  <text class="sub" x="40" y="236">放入后不要再改参与 hashCode / equals 的字段</text>
</svg>
"""

# Chapter 4
files["type-erasure.svg"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 280" role="img">
  <title>类型擦除</title>
  {STYLE}
  <text class="title" x="24" y="28">类型擦除：编译期有泛型，运行期大多只剩原始类型</text>

  <rect class="box-teal" x="60" y="70" width="200" height="60" rx="8"/><text class="node-text" x="95" y="106">List&lt;String&gt;</text>
  <line x1="260" y1="100" x2="340" y2="100" stroke="#334155" stroke-width="2.5" marker-end="url(#arrow)"/>
  <text class="sub" x="275" y="88">擦除</text>
  <rect class="box" x="340" y="70" width="160" height="60" rx="8"/><text class="node-text" x="390" y="106">List</text>

  <rect class="box-orange" x="60" y="160" width="200" height="60" rx="8"/><text class="node-text" x="90" y="196">List&lt;Integer&gt;</text>
  <line x1="260" y1="190" x2="340" y2="190" stroke="#334155" stroke-width="2.5" marker-end="url(#arrow)"/>
  <rect class="box" x="340" y="160" width="160" height="60" rx="8"/><text class="node-text" x="390" y="196">List</text>

  <text class="bad" x="530" y="100">不能 new T()</text>
  <text class="bad" x="530" y="130">不能 List&lt;int&gt;</text>
  <text class="bad" x="530" y="160">难做 instanceof List&lt;String&gt;</text>
  <text class="sub" x="530" y="200">运行时信息常靠 Class&lt;T&gt;</text>
</svg>
"""

files["pecs-wildcard.svg"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 280" role="img">
  <title>PECS：Producer Extends, Consumer Super</title>
  {STYLE}
  <text class="title" x="24" y="28">PECS：Producer Extends · Consumer Super</text>

  <rect class="panel" x="16" y="52" width="350" height="200" rx="10"/>
  <text class="title" x="36" y="84">? extends Number</text>
  <text class="ok" x="36" y="120">生产者：适合往外读</text>
  <text class="code" x="36" y="152">Number n = list.get(0);</text>
  <text class="bad" x="36" y="188">不能随意 add（除 null）</text>
  <text class="sub" x="36" y="220">实际可能是 List&lt;Integer&gt;</text>

  <rect class="panel" x="390" y="52" width="350" height="200" rx="10"/>
  <text class="title" x="410" y="84">? super Integer</text>
  <text class="ok" x="410" y="120">消费者：适合往里写</text>
  <text class="code" x="410" y="152">list.add(1);</text>
  <text class="sub" x="410" y="188">get 出来常是 Object</text>
  <text class="sub" x="410" y="220">实际可能是 List&lt;Number&gt;</text>
</svg>
"""

# Chapter 5
files["stream-pipeline.svg"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 320" role="img">
  <title>Stream 惰性管道</title>
  {STYLE}
  <text class="title" x="24" y="28">Stream：中间操作搭管道（惰性），终端操作才触发计算</text>

  <rect class="box-teal" x="260" y="60" width="220" height="44" rx="8"/><text class="node-text" x="310" y="88">创建 Stream</text>
  <line x1="370" y1="104" x2="370" y2="132" stroke="#0f766e" stroke-width="2" marker-end="url(#arrow-teal)"/>

  <rect class="box-blue" x="160" y="134" width="420" height="60" rx="8"/>
  <text class="node-text" x="200" y="160">filter / map / flatMap / sorted / peek …</text>
  <text class="sub" x="250" y="182">中间操作：只搭管道，不立刻算</text>
  <line x1="370" y1="194" x2="370" y2="222" stroke="#1d4ed8" stroke-width="2" marker-end="url(#arrow-blue)"/>

  <rect class="box-orange" x="160" y="224" width="420" height="60" rx="8"/>
  <text class="node-text" x="190" y="250">collect / toList / findFirst / count …</text>
  <text class="sub" x="230" y="272">终端操作：触发计算；之后 Stream 不可再用</text>
</svg>
"""

# Chapter 6
files["throwable-hierarchy.svg"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img">
  <title>Throwable 继承体系</title>
  {STYLE}
  <text class="title" x="24" y="28">异常体系：Throwable</text>

  <rect class="box" x="280" y="52" width="180" height="40" rx="8"/><text class="node-text" x="325" y="78">Throwable</text>
  <line x1="320" y1="92" x2="180" y2="130" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="400" y1="92" x2="520" y2="130" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>

  <rect class="box-rose" x="60" y="134" width="240" height="70" rx="8"/>
  <text class="node-text" x="145" y="164">Error</text>
  <text class="sub" x="80" y="188">OOM / StackOverflow · 别乱 catch</text>

  <rect class="box-blue" x="420" y="134" width="260" height="50" rx="8"/><text class="node-text" x="510" y="166">Exception</text>
  <line x1="500" y1="184" x2="400" y2="230" stroke="#1d4ed8" stroke-width="2" marker-end="url(#arrow-blue)"/>
  <line x1="580" y1="184" x2="640" y2="230" stroke="#1d4ed8" stroke-width="2" marker-end="url(#arrow-blue)"/>

  <rect class="box-amber" x="280" y="234" width="240" height="70" rx="8"/>
  <text class="node-text" x="310" y="264">RuntimeException</text>
  <text class="sub" x="300" y="288">非受检 · NPE / 业务异常</text>

  <rect class="box-teal" x="560" y="234" width="170" height="70" rx="8"/>
  <text class="node-text" x="585" y="264">其他 Exception</text>
  <text class="sub" x="580" y="288">受检 · IO / SQL</text>
</svg>
"""

for name, content in files.items():
    path = root / name
    path.write_text(content, encoding="utf-8")
    print("wrote", name)

print("total", len(files))
