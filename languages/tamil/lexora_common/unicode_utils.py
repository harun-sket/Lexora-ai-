"""
Lexora AI

Unicode Utilities

Shared by:
- TXT Refinery
- JSON Refinery
- OCR Pipeline
"""

from __future__ import annotations

import re
import unicodedata


ZERO_WIDTH = re.compile(
    r"[\u200B\u200C\u200D\u2060\uFEFF]"
)

MULTISPACE = re.compile(r"[ \t]+")

MULTIBLANK = re.compile(r"\n{3,}")


def normalize_unicode(text: str) -> str:
    """
    NFC normalization.

    Prevents broken Tamil combining characters.
    """
    return unicodedata.normalize("NFC", text)


def remove_zero_width(text: str) -> str:
    """
    Removes invisible Unicode characters.
    """
    return ZERO_WIDTH.sub("", text)


def normalize_whitespace(text: str) -> str:
    """
    Normalizes spaces and blank lines.
    """

    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    text = MULTISPACE.sub(" ", text)
    text = MULTIBLANK.sub("\n\n", text)

    return text.strip()


def basic_cleanup(text: str) -> str:
    """
    Universal cleanup.

    Every Lexora pipeline should call this first.
    """

    text = normalize_unicode(text)
    text = remove_zero_width(text)
    text = normalize_whitespace(text)

    return text
