"""
Lexora Quality Analyzer

Purpose
-------
Analyze text quality without modifying it.

This module provides metrics that help the Brain
decide which processing modules should run.
"""

from __future__ import annotations

import re


TAMIL_RE = re.compile(r"[\u0B80-\u0BFF]")
ENGLISH_RE = re.compile(r"[A-Za-z]")
NUMBER_RE = re.compile(r"\d")
REPLACEMENT_RE = re.compile(r"\uFFFD")


def analyze_quality(text: str) -> dict:
    total_chars = len(text)

    tamil_chars = len(TAMIL_RE.findall(text))
    english_chars = len(ENGLISH_RE.findall(text))
    numbers = len(NUMBER_RE.findall(text))
    replacement_chars = len(REPLACEMENT_RE.findall(text))

    blank_lines = sum(
        1
        for line in text.splitlines()
        if not line.strip()
    )

    multiple_spaces = len(
        re.findall(r"[ ]{2,}", text)
    )

    quality_score = 100

    quality_score -= replacement_chars * 15
    quality_score -= multiple_spaces * 2
    quality_score -= blank_lines

    quality_score = max(0, min(100, quality_score))

    return {
        "quality_score": quality_score,
        "characters": total_chars,
        "tamil_characters": tamil_chars,
        "english_characters": english_chars,
        "numeric_characters": numbers,
        "replacement_characters": replacement_chars,
        "blank_lines": blank_lines,
        "multiple_spaces": multiple_spaces,
    }
