# -*- coding: utf-8 -*-
from pathlib import Path
import importlib.util

root = Path(__file__).resolve().parent

svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 420" role="img" aria-labelledby="title desc">
  <title id="title">Java 方法参数只有值传递</title>
  <desc id="desc">基本类型拷贝值；引用类型拷贝引用副本。改对象字段可见，重绑形参不影响实参。</desc>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#0f766e"/>
    </marker>
    <style><![CDATA[
      .title { font: 700 15px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #0f172a; }
      .code { font: 600 12px ui-monospace, Consolas, monospace; fill: #334155; }
      .label { font: 12px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #475569; }
      .box-text { font: 600 13px ui-monospace, Consolas, monospace; fill: #0f172a; }
      .ok { font: 600 12px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #047857; }
      .bad { font: 600 12px 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; fill: #be123c; }
      .panel { fill: #f8fafc; stroke: #e2e8f0; stroke-width: 1.5; }
      .slot { fill: #ecfdf5; stroke: #0f766e; stroke-width: 2; }
      .obj { fill: #fff7ed; stroke: #c2410c; stroke-width: 2; }
    ]]></style>
  </defs>
  <text class="title" x="24" y="28">方法调用：传的永远是「副本」</text>
  <rect class="panel" x="16" y="44" width="688" height="120" rx="10"/>
  <text class="code" x="36" y="72">int n = 10;  bump(n);  // 形参拿到 10 的拷贝</text>
  <rect class="slot" x="36" y="90" width="100" height="48" rx="8"/>
  <text class="box-text" x="68" y="120">n=10</text>
  <text class="label" x="160" y="110">拷贝值</text>
  <rect class="slot" x="240" y="90" width="100" height="48" rx="8"/>
  <text class="box-text" x="262" y="120">a=10</text>
  <text class="bad" x="370" y="120">a=11 不会改回 n</text>
  <rect class="panel" x="16" y="180" width="688" height="210" rx="10"/>
  <text class="code" x="36" y="208">User u = ...;  rename(u);  // 形参拿到引用的拷贝</text>
  <rect class="slot" x="36" y="230" width="90" height="44" rx="8"/>
  <text class="box-text" x="58" y="258">u</text>
  <line x1="126" y1="252" x2="200" y2="252" stroke="#0f766e" stroke-width="2.5" marker-end="url(#arrow)"/>
  <rect class="obj" x="210" y="222" width="160" height="60" rx="8"/>
  <text class="box-text" x="230" y="258">User 对象</text>
  <rect class="slot" x="36" y="310" width="90" height="44" rx="8"/>
  <text class="box-text" x="48" y="338">param</text>
  <line x1="126" y1="332" x2="200" y2="252" stroke="#0f766e" stroke-width="2.5" marker-end="url(#arrow)"/>
  <text class="ok" x="400" y="250">param.name = Ada 可见</text>
  <text class="bad" x="400" y="290">param = new User() 不影响 u</text>
  <text class="label" x="400" y="330">两边起初指向同一对象；重绑只改副本</text>
</svg>
"""

path = root / "value-passing.svg"
path.write_text(svg, encoding="utf-8")

spec = importlib.util.spec_from_file_location("patch", root / "_patch_svg_dark.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
path.write_text(mod.patch_svg(path.read_text(encoding="utf-8")), encoding="utf-8")
text = path.read_text(encoding="utf-8")
assert "方法" in text and "prefers-color-scheme: dark" in text
print("wrote", path.name)
