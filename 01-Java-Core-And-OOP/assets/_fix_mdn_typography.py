# -*- coding: utf-8 -*-
"""Normalize bold / example fences / CJK-Latin spacing to MDN zh-CN style."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def annotate_example_fences(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    mode: str | None = None
    for line in lines:
        if re.match(r"^#### 错误写法", line):
            mode = "bad"
        elif re.match(r"^#### (正确写法|若需要)", line):
            mode = "good"
        elif line.startswith("```java") and mode:
            if "example-" not in line:
                tag = "java example-bad" if mode == "bad" else "java example-good"
                line = "```" + tag + line[len("```java") :]
            mode = None
        elif line.startswith("```"):
            mode = None
        out.append(line)
    return "".join(out)


def fix_spacing_outside_code(text: str) -> str:
    parts = re.split(r"(```.*?```)", text, flags=re.S)
    for i, part in enumerate(parts):
        if part.startswith("```"):
            continue
        new_lines = []
        for line in part.split("\n"):
            chunks = re.split(r"(`[^`]+`)", line)
            for j, ch in enumerate(chunks):
                if ch.startswith("`"):
                    continue
                ch = re.sub(r"([\u4e00-\u9fff])([A-Za-z])", r"\1 \2", ch)
                ch = re.sub(r"([A-Za-z])([\u4e00-\u9fff])", r"\1 \2", ch)
                ch = re.sub(r"([\u4e00-\u9fff])(\d)", r"\1 \2", ch)
                ch = re.sub(r"(\d)([\u4e00-\u9fff])", r"\1 \2", ch)
                ch = re.sub(r" ([，。；：、！？）】」』])", r"\1", ch)
                ch = re.sub(r"([（【「『]) ", r"\1", ch)
                chunks[j] = ch
            new_lines.append("".join(chunks))
        parts[i] = "\n".join(new_lines)
    text = "".join(parts)
    text = re.sub(r"\] \(", "](", text)
    return text


def fix_chapter(path: Path) -> None:
    s = path.read_text(encoding="utf-8")
    orig = s

    s = s.replace(
        "**Java 的强类型（更准确说：静态强类型）**做的是同一类事，而且更彻底：每个变量、参数、返回值在编译期都有确定类型；对不上，**编译失败，字节码都不会生成**。",
        "Java 的**强类型**（更准确说：静态强类型）做的是同一类事，而且更彻底：每个变量、参数、返回值在编译期都有确定类型；对不上就会**编译失败**，字节码都不会生成。",
    )
    s = s.replace(
        "Java 的 `final` 变量同理——**锁的是变量本身的绑定**，不是对象深度不可变。",
        "Java 的 `final` 变量同理——锁的是变量本身的**绑定**，不是对象深度不可变。",
    )
    s = s.replace(
        "Java 默认**不帮你搅类型**。",
        "Java 默认**不会**帮你随意做类型转换。",
    )

    # strip trailing fullwidth colon on headings
    s = re.sub(r"^(#{2,4} .+?)：\s*$", r"\1", s, flags=re.M)

    # table labels
    s = s.replace("| **前置** |", "| 前置 |")
    s = s.replace("| **学完应能** |", "| 学完应能 |")

    # leftover ❌ ✅ bold headers if any
    s = re.sub(r"\*\*❌ 错误写法：([^*]*)\*\*", r"#### 错误写法：\1", s)
    s = re.sub(r"\*\*✅ 正确写法：\*\*", "#### 正确写法", s)
    s = re.sub(r"\*\*✅ 正确写法：([^*]*)\*\*", r"#### 正确写法：\1", s)
    s = re.sub(r"\*\*([^*\n]{2,40}：)\*\*\s*$", r"#### \1", s, flags=re.M)

    s = annotate_example_fences(s)
    s = fix_spacing_outside_code(s)

    # primary API intros: already mostly backticks; promote a few definition sites
    replacements = {
        "对不上会在**编译期**被拦住": "对不上会在**编译期**被拦住",
        "当前方法的**栈帧**里": "当前方法的**栈帧**里",
    }
    for a, b in replacements.items():
        s = s.replace(a, b)

    if s != orig:
        path.write_text(s, encoding="utf-8")
        print("updated", path.name)
    else:
        print("unchanged", path.name)


def main() -> None:
    for name in [
        "01-strong-typing-and-basics.md",
        "00-install-jdk-and-toolchain.md",
        "02-oop-deep-dive.md",
        "03-collections-framework.md",
        "04-generics.md",
        "05-stream-and-lambda.md",
        "06-exception-system.md",
        "index.md",
    ]:
        path = ROOT / name
        if path.exists():
            fix_chapter(path)


if __name__ == "__main__":
    main()
