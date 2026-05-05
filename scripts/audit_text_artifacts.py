#!/usr/bin/env python3
"""Heuristic artifact audit for scientific AI-pattern editing.

This is not an AI detector and does not produce a score. It only flags mechanical
issues that are easy to miss during manuscript editing: hidden Unicode, odd
spacing, repeated phrases, and clusters of generic AI-associated wording.
"""

from __future__ import annotations

import argparse
import collections
import re
import sys
import unicodedata
from pathlib import Path


WATCH_TERMS = [
    "crucial",
    "comprehensive",
    "robust",
    "significant",
    "important",
    "key",
    "pivotal",
    "novel",
    "highlight",
    "highlights",
    "highlighting",
    "underscore",
    "underscores",
    "underscoring",
    "landscape",
    "framework",
    "leverage",
    "enhance",
    "facilitate",
    "shed light",
    "delve",
    "worth noting",
    "important to note",
    "serves as",
    "plays a role",
    "paves the way",
    "holds promise",
]

ODD_SPACE_CODEPOINTS = {
    0x00A0,
    0x1680,
    0x180E,
    0x2000,
    0x2001,
    0x2002,
    0x2003,
    0x2004,
    0x2005,
    0x2006,
    0x2007,
    0x2008,
    0x2009,
    0x200A,
    0x200B,
    0x200C,
    0x200D,
    0x202F,
    0x205F,
    0x2060,
    0x3000,
    0xFEFF,
}

STOPWORDS = {
    "the",
    "and",
    "that",
    "this",
    "with",
    "from",
    "were",
    "was",
    "are",
    "for",
    "of",
    "in",
    "to",
    "by",
    "as",
    "on",
    "we",
    "our",
    "a",
    "an",
}


def line_col(text: str, index: int) -> tuple[int, int]:
    line = text.count("\n", 0, index) + 1
    last_newline = text.rfind("\n", 0, index)
    col = index + 1 if last_newline == -1 else index - last_newline
    return line, col


def audit_unicode(text: str) -> list[str]:
    findings = []
    for index, char in enumerate(text):
        code = ord(char)
        category = unicodedata.category(char)
        if code in ODD_SPACE_CODEPOINTS or (category.startswith("C") and char not in "\n\r\t"):
            line, col = line_col(text, index)
            name = unicodedata.name(char, "UNKNOWN")
            findings.append(f"line {line}, col {col}: U+{code:04X} {name}")
    return findings


def audit_spacing(text: str) -> list[str]:
    findings = []
    patterns = [
        ("missing space after sentence punctuation", re.compile(r"[.!?][A-Z]")),
        ("multiple internal spaces", re.compile(r"(?<!\n) {2,}(?!\n)")),
        ("space before punctuation", re.compile(r" +[,.;:]")),
    ]
    for label, pattern in patterns:
        for match in pattern.finditer(text):
            line, col = line_col(text, match.start())
            excerpt = text[match.start() : match.end()]
            findings.append(f"line {line}, col {col}: {label}: {excerpt!r}")
    return findings


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z][A-Za-z'-]*", text.lower())


def audit_repeated_phrases(text: str) -> list[str]:
    tokens = [word for word in words(text) if word not in STOPWORDS]
    findings = []
    for n in (3, 4, 5):
        counts: collections.Counter[tuple[str, ...]] = collections.Counter(
            tuple(tokens[i : i + n]) for i in range(0, max(0, len(tokens) - n + 1))
        )
        for phrase, count in counts.most_common():
            if count >= 3:
                findings.append(f"{count}x repeated {n}-word phrase: {' '.join(phrase)}")
    return findings[:20]


def audit_watch_terms(text: str) -> list[str]:
    lowered = text.lower()
    findings = []
    for term in WATCH_TERMS:
        count = len(re.findall(rf"\b{re.escape(term)}\b", lowered))
        if count:
            findings.append(f"{count}x watch term: {term}")
    return findings


def print_section(title: str, findings: list[str]) -> None:
    print(f"\n## {title}")
    if not findings:
        print("No issues found.")
        return
    for item in findings:
        print(f"- {item}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit text for mechanical AI-humanizer artifacts.")
    parser.add_argument("path", nargs="?", help="Text file to audit. Reads stdin if omitted.")
    args = parser.parse_args()

    if args.path:
        text = Path(args.path).read_text(encoding="utf-8")
    else:
        text = sys.stdin.read()

    print("# Text Artifact Audit")
    print("This is a heuristic manuscript-editing aid, not an AI detector and not a score.")
    print_section("Hidden or unusual Unicode", audit_unicode(text))
    print_section("Spacing artifacts", audit_spacing(text))
    print_section("Repeated phrases", audit_repeated_phrases(text))
    print_section("Context-sensitive watch terms", audit_watch_terms(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
