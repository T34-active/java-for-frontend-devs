# -*- coding: utf-8 -*-
from pathlib import Path

root = Path(__file__).resolve().parent

primitive = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 520" role="img" aria-labelledby="title desc">
  <title id="title">基本类型、包装类型与 null 引用</title>
  <desc id="desc">对比 int 槽位直接存值、Integer 引用指向堆对象、以及 null 不指向任何对象。</desc>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#0f766e"/>
    </marker>
    <style><![CDATA[
      .title { font: 700 16px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #0f172a; }
      .code { font: 600 13px ui-monospace, Consolas, monospace; fill: #334155; }
      .label { font: 12px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #475569; }
      .box-text { font: 600 14px ui-monospace, Consolas, monospace; fill: #0f172a; }
      .hint { font: 12px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #64748b; }
      .panel { fill: #f8fafc; stroke: #e2e8f0; stroke-width: 1.5; }
      .slot { fill: #ecfdf5; stroke: #0f766e; stroke-width: 2; }
      .obj { fill: #fff7ed; stroke: #c2410c; stroke-width: 2; }
      .null-slot { fill: #f1f5f9; stroke: #94a3b8; stroke-width: 2; stroke-dasharray: 6 4; }
    ]]></style>
  </defs>
  <rect class="panel" x="16" y="16" width="688" height="140" rx="12"/>
  <text class="title" x="36" y="44">【基本类型】</text>
  <text class="code" x="36" y="72">int count = 42;</text>
  <rect class="slot" x="36" y="92" width="120" height="44" rx="8"/>
  <text class="box-text" x="76" y="120">42</text>
  <text class="hint" x="172" y="120">槽位里就是比特值本身（不是对象）</text>
  <rect class="panel" x="16" y="172" width="688" height="170" rx="12"/>
  <text class="title" x="36" y="200">【引用类型 / 包装类型】</text>
  <text class="code" x="36" y="228">Integer boxed = 42;  // 自动装箱 ≈ Integer.valueOf(42)</text>
  <rect class="slot" x="36" y="252" width="120" height="56" rx="8"/>
  <text class="box-text" x="62" y="286">引用</text>
  <line x1="156" y1="280" x2="280" y2="280" stroke="#0f766e" stroke-width="2.5" marker-end="url(#arrow)"/>
  <rect class="obj" x="290" y="244" width="200" height="72" rx="8"/>
  <text class="box-text" x="318" y="274">Integer 对象</text>
  <text class="label" x="318" y="298">内部值 = 42</text>
  <text class="hint" x="510" y="280">堆上的对象</text>
  <rect class="panel" x="16" y="358" width="688" height="142" rx="12"/>
  <text class="title" x="36" y="386">【空引用】</text>
  <text class="code" x="36" y="414">Integer missing = null;</text>
  <rect class="null-slot" x="36" y="434" width="120" height="44" rx="8"/>
  <text class="box-text" x="66" y="462">null</text>
  <text class="hint" x="172" y="462">没有箭头，不指向任何对象</text>
</svg>
"""

unbox = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 300" role="img" aria-labelledby="title desc">
  <title id="title">对 null 包装类型拆箱导致 NPE</title>
  <desc id="desc">拆箱时编译器插入 intValue，missing 为 null 则抛出 NullPointerException。</desc>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#be123c"/>
    </marker>
    <style><![CDATA[
      .title { font: 700 15px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #0f172a; }
      .code { font: 600 13px ui-monospace, Consolas, monospace; fill: #334155; }
      .node-text { font: 600 13px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #0f172a; }
      .node { fill: #fff1f2; stroke: #e11d48; stroke-width: 2; }
      .node-mid { fill: #fff7ed; stroke: #ea580c; stroke-width: 2; }
      .node-start { fill: #f8fafc; stroke: #64748b; stroke-width: 2; }
    ]]></style>
  </defs>
  <text class="title" x="24" y="32">拆箱时若引用是 null</text>
  <text class="code" x="24" y="56">int raw = missing;</text>
  <rect class="node-start" x="160" y="76" width="400" height="48" rx="8"/>
  <text class="node-text" x="220" y="106">源码：int raw = missing</text>
  <line x1="360" y1="124" x2="360" y2="152" stroke="#be123c" stroke-width="2.5" marker-end="url(#arrow)"/>
  <rect class="node-mid" x="160" y="154" width="400" height="48" rx="8"/>
  <text class="node-text" x="200" y="184">编译器插入 missing.intValue()</text>
  <line x1="360" y1="202" x2="360" y2="230" stroke="#be123c" stroke-width="2.5" marker-end="url(#arrow)"/>
  <rect class="node" x="80" y="232" width="560" height="48" rx="8"/>
  <text class="node-text" x="120" y="262" fill="#be123c">missing 为 null → 调用实例方法 → NullPointerException</text>
</svg>
"""

listing = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 340" role="img" aria-labelledby="title desc">
  <title id="title">为什么 List 只能装 Integer</title>
  <desc id="desc">List 格子存对象引用，可放 Integer，不能放裸 int；add(1) 时先自动装箱。</desc>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#1d4ed8"/>
    </marker>
    <style><![CDATA[
      .title { font: 700 15px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #0f172a; }
      .node-text { font: 600 13px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #0f172a; }
      .ok { font: 600 13px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #047857; }
      .bad { font: 600 13px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #be123c; }
      .cell { fill: #eff6ff; stroke: #2563eb; stroke-width: 2; }
      .step { fill: #f8fafc; stroke: #cbd5e1; stroke-width: 1.5; }
    ]]></style>
  </defs>
  <text class="title" x="24" y="32">集合为何只要包装类型</text>
  <rect class="step" x="24" y="52" width="672" height="44" rx="8"/>
  <text class="node-text" x="40" y="80">1. List 内部 ≈ 对象引用数组（格子里放的是箭头，不是裸 int 比特）</text>
  <line x1="360" y1="96" x2="360" y2="118" stroke="#1d4ed8" stroke-width="2" marker-end="url(#arrow)"/>
  <rect class="cell" x="120" y="124" width="72" height="56" rx="6"/>
  <rect class="cell" x="200" y="124" width="72" height="56" rx="6"/>
  <rect class="cell" x="280" y="124" width="72" height="56" rx="6"/>
  <text class="node-text" x="138" y="158">引用</text>
  <text class="node-text" x="218" y="158">引用</text>
  <text class="node-text" x="298" y="158">引用</text>
  <text class="ok" x="380" y="148">可指向 Integer</text>
  <text class="bad" x="380" y="172">放不进裸 int</text>
  <line x1="360" y1="180" x2="360" y2="202" stroke="#1d4ed8" stroke-width="2" marker-end="url(#arrow)"/>
  <rect class="step" x="24" y="206" width="672" height="44" rx="8"/>
  <text class="node-text" x="40" y="234">2. int 不是 Object 子类型 → 不能写 List&lt;int&gt;</text>
  <line x1="360" y1="250" x2="360" y2="272" stroke="#1d4ed8" stroke-width="2" marker-end="url(#arrow)"/>
  <rect class="step" x="24" y="276" width="672" height="44" rx="8"/>
  <text class="node-text" x="40" y="304">3. 正确：List&lt;Integer&gt;；add(1) 时先 Integer.valueOf(1) 再放入引用</text>
</svg>
"""

pipeline = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 440" role="img" aria-labelledby="title desc">
  <title id="title">从源码到运行的类型检查流水线</title>
  <desc id="desc">源码经编译类型检查，失败则无程序；通过后生成字节码，JVM 从 main 入口执行。</desc>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#334155"/>
    </marker>
    <style><![CDATA[
      .title { font: 700 15px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #0f172a; }
      .node-text { font: 600 13px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #0f172a; }
      .side { font: 600 12px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #be123c; }
      .ok { font: 600 12px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #047857; }
      .node { fill: #f8fafc; stroke: #64748b; stroke-width: 2; }
      .check { fill: #ecfdf5; stroke: #0f766e; stroke-width: 2; }
      .fail { fill: #fff1f2; stroke: #e11d48; stroke-width: 2; }
    ]]></style>
  </defs>
  <text class="title" x="24" y="32">写代码 → 运行（强类型卡在编译期）</text>
  <rect class="node" x="200" y="52" width="320" height="40" rx="8"/>
  <text class="node-text" x="280" y="78">你写下源码 .java</text>
  <line x1="360" y1="92" x2="360" y2="118" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>
  <rect class="check" x="200" y="120" width="320" height="40" rx="8"/>
  <text class="node-text" x="240" y="146">javac / Maven 编译 · 类型检查</text>
  <line x1="520" y1="140" x2="560" y2="140" stroke="#e11d48" stroke-width="2" marker-end="url(#arrow)"/>
  <rect class="fail" x="560" y="120" width="140" height="40" rx="8"/>
  <text class="side" x="575" y="146">失败 → 无程序</text>
  <text class="ok" x="372" y="178">通过</text>
  <line x1="360" y1="160" x2="360" y2="198" stroke="#047857" stroke-width="2" marker-end="url(#arrow)"/>
  <rect class="node" x="200" y="200" width="320" height="40" rx="8"/>
  <text class="node-text" x="280" y="226">生成 .class 字节码</text>
  <line x1="360" y1="240" x2="360" y2="268" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>
  <rect class="node" x="200" y="270" width="320" height="40" rx="8"/>
  <text class="node-text" x="290" y="296">java 启动 JVM</text>
  <line x1="360" y1="310" x2="360" y2="338" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>
  <rect class="node" x="160" y="340" width="400" height="40" rx="8"/>
  <text class="node-text" x="200" y="366">找到 public static void main(String[] args)</text>
  <line x1="360" y1="380" x2="360" y2="400" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>
  <text class="node-text" x="250" y="420">按顺序执行方法体里的语句</text>
</svg>
"""

files = {
    "primitive-vs-wrapper.svg": primitive,
    "unbox-npe.svg": unbox,
    "list-needs-integer.svg": listing,
    "compile-pipeline.svg": pipeline,
}

for name, content in files.items():
    path = root / name
    path.write_text(content, encoding="utf-8")
    text = path.read_text(encoding="utf-8")
    assert "基本" in text or "拆箱" in text or "集合" in text or "写代码" in text, name
    print("wrote", name)

# 统一注入暗色 CSS 变量（与站点黑夜模式对齐）
from _patch_svg_dark import patch_svg  # noqa: E402

for name in files:
    path = root / name
    path.write_text(patch_svg(path.read_text(encoding="utf-8")), encoding="utf-8")
    print("dark-patched", name)
