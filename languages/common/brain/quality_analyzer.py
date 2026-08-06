"""
Lexora AI
Quality Analyzer

Analyzes raw text and returns metrics that the
Lexora Brain uses for routing decisions.
"""

from __future__ import annotations

import re
from collections import Counter


NOISE_PATTERN = re.compile(r"[#@%$^&*_~=<>|]+")


def analyze_text(text: str) -> dict:
    text = text or ""

    lines = text.splitlines()

    non_empty_lines = [line.strip() for line in lines if line.strip()]

    duplicate_lines = sum(
        count - 1
        for count in Counter(non_empty_lines).values()
        if count > 1
    )

    noise_matches = NOISE_PATTERN.findall(text)
    noise_characters = sum(len(match) for match in noise_matches)

    whitespace_characters = sum(
        1 for char in text if char.isspace()
    )

    characters = len(text)

    words = len(text.split())

    return {
        "characters": characters,
        "words": words,
        "lines": len(lines),
        "non_empty_lines": len(non_empty_lines),
        "duplicate_lines": duplicate_lines,
        "noise_characters": noise_characters,
        "whitespace_characters": whitespace_characters,
        "noise_ratio": (
            round(noise_characters / characters, 4)
            if characters
            else 0.0
        ),
    }
