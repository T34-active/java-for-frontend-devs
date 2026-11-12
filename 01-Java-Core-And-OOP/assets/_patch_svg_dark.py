# -*- coding: utf-8 -*-
"""为 assets/*.svg 注入暗色模式：CSS 变量 + prefers-color-scheme。"""
from __future__ import annotations

import re
from pathlib import Path

root = Path(__file__).resolve().parent

COLOR_TO_VAR = {
    "#0f172a": "--c-text",
    "#334155": "--c-muted",
    "#475569": "--c-soft",
    "#64748b": "--c-hint",
    "#94a3b8": "--c-null-stroke",
    "#f8fafc": "--c-panel",
    "#f1f5f9": "--c-null-fill",
    "#e2e8f0": "--c-panel-stroke",
    "#cbd5e1": "--c-step-stroke",
    "#ecfdf5": "--c-teal-fill",
    "#0f766e": "--c-teal",
    "#047857": "--c-ok",
    "#fff7ed": "--c-orange-fill",
    "#c2410c": "--c-orange",
    "#ea580c": "--c-orange-mid",
    "#fff1f2": "--c-rose-fill",
    "#e11d48": "--c-rose",
    "#be123c": "--c-bad",
    "#eff6ff": "--c-blue-fill",
    "#2563eb": "--c-blue",
    "#1d4ed8": "--c-blue-deep",
    "#fffbeb": "--c-amber-fill",
    "#d97706": "--c-amber",
}

DARK_VARS = """\
:root {
  color-scheme: light dark;
  --c-text: #0f172a;
  --c-muted: #334155;
  --c-soft: #475569;
  --c-hint: #64748b;
  --c-null-stroke: #94a3b8;
  --c-panel: #f8fafc;
  --c-null-fill: #f1f5f9;
  --c-panel-stroke: #e2e8f0;
  --c-step-stroke: #cbd5e1;
  --c-teal-fill: #ecfdf5;
  --c-teal: #0f766e;
  --c-ok: #047857;
  --c-orange-fill: #fff7ed;
  --c-orange: #c2410c;
  --c-orange-mid: #ea580c;
  --c-rose-fill: #fff1f2;
  --c-rose: #e11d48;
  --c-bad: #be123c;
  --c-blue-fill: #eff6ff;
  --c-blue: #2563eb;
  --c-blue-deep: #1d4ed8;
  --c-amber-fill: #fffbeb;
  --c-amber: #d97706;
}
@media (prefers-color-scheme: dark) {
  :root {
    --c-text: #e2e8f0;
    --c-muted: #cbd5e1;
    --c-soft: #94a3b8;
    --c-hint: #94a3b8;
    --c-null-stroke: #64748b;
    --c-panel: #1e293b;
    --c-null-fill: #334155;
    --c-panel-stroke: #334155;
    --c-step-stroke: #475569;
    --c-teal-fill: #134e4a;
    --c-teal: #2dd4bf;
    --c-ok: #34d399;
    --c-orange-fill: #7c2d12;
    --c-orange: #fb923c;
    --c-orange-mid: #fb923c;
    --c-rose-fill: #881337;
    --c-rose: #fb7185;
    --c-bad: #fb7185;
    --c-blue-fill: #1e3a8a;
    --c-blue: #60a5fa;
    --c-blue-deep: #60a5fa;
    --c-amber-fill: #78350f;
    --c-amber: #fbbf24;
  }
}
"""

MARKER = "color-scheme: light dark;"


def hex_to_var(raw: str) -> str:
    var = COLOR_TO_VAR.get(raw.lower())
    return f"var({var})" if var else raw


def rewrite_colors(text: str) -> str:
    return re.sub(
        r"#[0-9A-Fa-f]{6}",
        lambda m: hex_to_var(m.group(0)),
        text,
    )


def strip_old_dark_block(body: str) -> str:
    if MARKER not in body:
        return body
    # 删除从首次 :root { color-scheme... 到对应 @media 块结束
    start = body.find(":root")
    if start < 0:
        return body
    media = body.find("@media (prefers-color-scheme: dark)", start)
    if media < 0:
        return body
    # 找到 media 块的结束：从 media 起数大括号
    i = body.find("{", media)
    depth = 0
    end = None
    for idx in range(i, len(body)):
        ch = body[idx]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end = idx + 1
                break
    if end is None:
        return body
    return body[:start] + body[end:]


def patch_style_body(body: str) -> str:
    body = strip_old_dark_block(body)
    # 变量块本身含亮色 hex，先注入再改其余规则
    rest = rewrite_colors(body.lstrip())
    return DARK_VARS + rest


def patch_svg(content: str) -> str:
    style_re = re.compile(
        r"(<style><!\[CDATA\[)(.*?)(\]\]></style>)",
        re.DOTALL,
    )
    m = style_re.search(content)
    if not m:
        raise ValueError("no style CDATA block")

    new_body = patch_style_body(m.group(2))
    content = content[: m.start(2)] + new_body + content[m.end(2) :]

    def rewrite_attr(match: re.Match[str]) -> str:
        attr, quote, value = match.group(1), match.group(2), match.group(3)
        mapped = hex_to_var(value)
        if mapped == value:
            return match.group(0)
        return f"{attr}={quote}{mapped}{quote}"

    content = re.sub(
        r'\b(fill|stroke)=([\'"])(#[0-9A-Fa-f]{6})\2',
        rewrite_attr,
        content,
    )
    return content


def main() -> None:
    for path in sorted(root.glob("*.svg")):
        raw = path.read_text(encoding="utf-8")
        try:
            patched = patch_svg(raw)
        except ValueError as exc:
            print("skip", path.name, exc)
            continue
        path.write_text(patched, encoding="utf-8")
        leftover = [
            c
            for c in re.findall(r"#[0-9A-Fa-f]{6}", patched)
            if c.lower() in COLOR_TO_VAR
            and "--c-" not in patched[max(0, patched.lower().find(c.lower()) - 30) : patched.lower().find(c.lower())]
        ]
        # 变量定义里会保留 hex，属正常；属性/规则里不应再有未映射的调色板色
        print("patched", path.name)


if __name__ == "__main__":
    main()
