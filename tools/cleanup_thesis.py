#!/usr/bin/env python3
"""Clean pandoc/LaTeX artifacts from thesis markdown."""

import re
import sys
from pathlib import Path


def clean_pandoc_references(text: str) -> str:
    # Pandoc attribute blocks spanning multiple lines
    text = re.sub(
        r"\{reference-type=\"[^\"]+\"(?:\s*\n\s*reference=\"[^\"]+\")?\s*\}",
        "",
        text,
    )
    # Standalone bracket cross-refs left after attribute removal
    text = re.sub(r"\[\[[^\]]+\]\]\([^)]+\)", "", text)
    text = re.sub(r"(?:Figure|Table|Section|Appendix|Chapter|Panel|Equation)\s*\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"shown in\s*\n\s*\.", "shown below.", text)
    text = re.sub(r"summarizes the major dependencies\s*\n\s*at a glance\.", "summarizes the major dependencies at a glance.", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text


def clean_citations(text: str) -> str:
    return re.sub(r"\s*\[@(?:[^\]]+)\]", "", text)


def clean_header_ids(text: str) -> str:
    return re.sub(r"\s*\{#[^}]+\}", "", text)


def clean_smallcaps(text: str) -> str:
    return re.sub(r"\[([^\]]+)\]\{\.smallcaps\}", r"\1", text)


def clean_trailing_backslashes(text: str) -> str:
    return re.sub(r"\\(\s*)$", r"\1", text, flags=re.MULTILINE)


def clean_spacing_artifacts(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if re.match(r"^#{1,6}\s+0pt\s*$", line):
            continue
        if re.match(r"^\d+pt plus .*", line):
            continue
        lines.append(line)
    return "\n".join(lines)


def clean_math_labels(text: str) -> str:
    text = re.sub(r"\\label\{[^}]+\}", "", text)
    text = re.sub(r"\$\$\\begin\{equation\}", "$$", text)
    text = re.sub(r"\\end\{equation\}\$\$", "$$", text)
    text = re.sub(
        r"<span class=\"math inline\">([^<]*)</span>",
        lambda m: f"${m.group(1).strip()}$" if m.group(1).strip() else "",
        text,
    )
    return text


def clean_code_fences(text: str) -> str:
    def repl(match: re.Match) -> str:
        info = match.group(1)
        lang = info.split()[0].lstrip(".") if info else ""
        if lang in {"bash", "c", "text", "python", "sh"}:
            return f"```{lang}"
        return "```"

    return re.sub(r"``` \{([^}]+)\}", repl, text)


def clean_figure_blocks(text: str) -> str:
    def figure_repl(match: re.Match) -> str:
        block = match.group(0)
        caption = re.search(r"<figcaption>(.*?)</figcaption>", block, re.DOTALL)
        inner = re.sub(r"<figure[^>]*>|</figure>|<div[^>]*>|</div>", "", block)
        inner = re.sub(r"<figcaption>.*?</figcaption>", "", inner, flags=re.DOTALL)
        if inner.strip():
            if caption:
                return f"\n*{caption.group(1).strip()}*\n"
            return block
        if caption:
            cap = caption.group(1).strip()
            cap = re.sub(r"<span class=\"math inline\">([^<]*)</span>", r"$\1$", cap)
            return f"\n*{cap}*\n"
        return ""

    return re.sub(r"<figure[^>]*>.*?</figure>", figure_repl, text, flags=re.DOTALL)


def clean_chess_diagram_debris(text: str) -> str:
    lines = []
    skip_fen = False
    fen_re = re.compile(
        r"^[rnbqkpRNBQKP1-8/].*\s(w|b)\s+[KQkq-]+\s+-"
    )
    debris_re = re.compile(
        r"^(fstyle=|lor=red,|markfields=|\d+/[0-9a-zA-Z/]+\s+(w|b)\s+)"
    )
    orphan_caption_re = re.compile(
        r"^(Defence|example|movement|Opera Game|checkmate|castling|Caro-Kann|enpassant|"
        r"kingmovement|queenmovement|rookmovement|bishopmovement|knightmovement|operamate|"
        r"carokann)\b",
        re.I,
    )

    for line in text.splitlines():
        stripped = line.strip()
        if debris_re.match(stripped) or fen_re.match(stripped):
            skip_fen = True
            continue
        if skip_fen:
            if not stripped:
                skip_fen = False
                lines.append(line)
                continue
            if fen_re.match(stripped) or orphan_caption_re.match(stripped):
                continue
            skip_fen = False
        if stripped in {"*p*", "*c*"}:
            continue
        if orphan_caption_re.match(stripped) and len(stripped.split()) <= 4:
            continue
        lines.append(line)
    return "\n".join(lines)


def convert_abbreviations(text: str) -> str:
    def repl(match: re.Match) -> str:
        body = match.group(1)
        rows = ["| Abbreviation | Meaning |", "| --- | --- |"]
        for line in body.splitlines():
            line = line.strip().rstrip("\\")
            if not line or line == "tabbing":
                continue
            m = re.match(r"^(\S+)\s+(.+)$", line)
            if m:
                abbr, desc = m.group(1), m.group(2)
                abbr = abbr.replace("P̄rincipal", "Principal")
                rows.append(f"| {abbr} | {desc} |")
        return "\n".join(rows) + "\n"

    return re.sub(
        r"## Abbreviations\n\n(?::: tabbing\n| tabbing\n)(.*?):::\n*",
        lambda m: "## Abbreviations\n\n" + repl(m),
        text,
        flags=re.DOTALL,
    )


def convert_tabular_block(text: str) -> str:
    def repl(match: re.Match) -> str:
        body = match.group(1).strip()
        lines = [ln.rstrip("\\").strip() for ln in body.splitlines() if ln.strip()]
        if not lines:
            return ""

        if any(ln.startswith("|") for ln in lines):
            cleaned = []
            for ln in lines:
                if ln.startswith(": "):
                    cleaned.append(f"\n*{ln[2:].strip()}*\n")
                elif not re.match(r"^@?l\s", ln) and not ln.startswith("S[table"):
                    cleaned.append(ln)
            return "\n".join(cleaned) + "\n"

        rows = []
        for ln in lines:
            if ln.startswith("S[table") or re.match(r"^@?l\s", ln):
                continue
            if "&" in ln:
                cells = [c.strip() for c in ln.split("&")]
                rows.append("| " + " | ".join(cells) + " |")
            elif ln.startswith(": "):
                rows.append(f"\n*{ln[2:].strip()}*\n")

        if len(rows) < 1:
            return "\n".join(rows) + "\n"

        ncol = rows[0].count("|") - 1
        sep = "| " + " | ".join(["---"] * ncol) + " |"
        if len(rows) == 1:
            return rows[0] + "\n" + sep + "\n"
        return rows[0] + "\n" + sep + "\n" + "\n".join(rows[1:]) + "\n"

    return re.sub(r"::: (?:\{#[^}]+\}|tabular)\n(.*?):::", repl, text, flags=re.DOTALL)


def clean_div_blocks(text: str) -> str:
    text = re.sub(r"::: minipage\n(.*?):::\n*", r"\1\n\n", text, flags=re.DOTALL)
    text = re.sub(r"^:::\s*$", "", text, flags=re.MULTILINE)
    return text


def clean_latex_artifacts(text: str) -> str:
    text = re.sub(r"\[\]\{#([^ ]+)(?:\s+label=\"[^\"]+\")?\}", "", text)
    text = re.sub(r"`<!-- -->`\{=html\}", "", text)
    text = re.sub(r"\(\\the\\numexpr \(5000\)/2\\relax pairs\)", "(2500 pairs)", text)
    text = re.sub(r"\*\<\<(.*?)\>\>\*", r"*\1*", text)
    text = re.sub(r"P̄rincipal", "Principal", text)
    # Fix broken align line continuations in equations
    text = re.sub(r", & \\$", ", &", text)
    text = re.sub(r"<strong>(.*?)</strong>", r"**\1**", text)
    return text


def fix_broken_math_lines(text: str) -> str:
    text = re.sub(r"\$8 \\times\n8\$", r"$8 \\times 8$", text)
    text = re.sub(
        r"`position \[fen `\*`fenstring`\*` \| startpos\] moves `\$move_1 \\dots\s*\nmove_i\$",
        "`position [fen <fen> | startpos] moves <move_1> ... <move_i>`",
        text,
    )
    return text


def replace_front_matter(text: str) -> str:
    m = re.match(r"(---\n.*?\n---\n)(.*)(# Introduction)", text, flags=re.DOTALL)
    if not m:
        return text

    front, old, _ = m.group(1), m.group(2), m.group(3)

    def section(name: str, end: str) -> str:
        pat = rf"\*\*{re.escape(name)}\*\*\\?\n+(.*?)\*\*{re.escape(end)}\*\*"
        hit = re.search(pat, old, re.DOTALL)
        return hit.group(1).strip() if hit else ""

    prologue = section("Prologue", "Abstract")
    abstract = section("Abstract", "Περίληψη")
    abstract = re.sub(r"::: minipage\n(.*?):::\n*", "", abstract, flags=re.DOTALL).strip()
    # Greek block may follow minipage
    greek = re.search(
        r"\*\*Περίληψη\*\*\\?\n+(.*?)\*\*Acknowledgments\*\*",
        old,
        re.DOTALL,
    )
    greek = greek.group(1).strip() if greek else ""
    greek = re.sub(r"::: minipage\n(.*?):::\n*", r"\1\n", greek, flags=re.DOTALL)

    ack = section("Acknowledgments", "Abbreviations")
    body_after = text.split("# Introduction", 1)[1]

    return (
        front
        + """
![IHU Logo](/assets/ihu-logo-gr.png)

**International Hellenic University** — School of Engineering  
Department of Information and Electronic Engineering  
**Diploma Thesis** (Code: 25331)

**Student:** Konstantinos Despoinidis (ID: 2021035)  
**Supervisor:** Professor Panagiotis Tzekis  
**Completed:** 2 June 2026

![Die Schachspieler](/assets/painting.jpg)

*Dedicated to my parents.*

## Prologue

"""
        + prologue
        + """

## Abstract

"""
        + abstract
        + """

## Περίληψη

"""
        + greek
        + """

## Acknowledgments

"""
        + ack
        + """

## Abbreviations

PLACEHOLDER_ABBREVIATIONS

# Introduction"""
        + body_after
    )


def main() -> None:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "_posts/2026-06-02-thesis.md")
    text = path.read_text(encoding="utf-8")
    text = text.replace("date: 2026-6-2", "date: 2026-06-02")

    # Extract abbreviations before front matter replacement destroys them
    abbr_match = re.search(r"::: tabbing\n(.*?):::", text, re.DOTALL)
    abbr_table = ""
    if abbr_match:
        rows = ["| Abbreviation | Meaning |", "| --- | --- |"]
        for line in abbr_match.group(1).splitlines():
            line = line.strip().rstrip("\\")
            if not line:
                continue
            parts = re.split(r"\s{2,}|\t", line, maxsplit=1)
            if len(parts) == 1:
                m = re.match(r"^(\S+)\s+(.+)$", line)
                if m:
                    parts = [m.group(1), m.group(2)]
            if len(parts) == 2:
                rows.append(f"| {parts[0]} | {parts[1]} |")
        abbr_table = "\n".join(rows) + "\n"

    text = replace_front_matter(text)
    text = text.replace("PLACEHOLDER_ABBREVIATIONS\n", abbr_table)

    text = clean_trailing_backslashes(text)
    text = clean_smallcaps(text)
    text = clean_header_ids(text)
    text = clean_spacing_artifacts(text)
    text = fix_broken_math_lines(text)
    text = clean_div_blocks(text)
    text = clean_pandoc_references(text)
    text = clean_citations(text)
    text = clean_math_labels(text)
    text = clean_code_fences(text)
    text = clean_figure_blocks(text)
    text = clean_chess_diagram_debris(text)
    text = convert_tabular_block(text)
    text = convert_abbreviations(text)
    text = clean_latex_artifacts(text)

    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    path.write_text(text, encoding="utf-8")
    print(f"Cleaned {path} ({len(text.splitlines())} lines)")


if __name__ == "__main__":
    main()
