"""
Lexora AI

Unicode Repair

Fixes:
- Unicode normalization
- Zero-width characters
- BOM
- Replacement characters
- Common mojibake
"""

import re
import unicodedata


ZERO_WIDTH = re.compile(
    r"[\u200B\u200C\u200D\u2060\uFEFF]"
)


MOJIBAKE = {
    "ï»¿": "",
    "â€™": "'",
    "â€œ": '"',
    "â€": '"',
    "â€“": "-",
    "â€”": "-",
    "Â": "",
    "Ã": "",
    "�": "",
}


def repair_unicode(text: str) -> str:
    if not text:
        return ""

    text = unicodedata.normalize(
        "NFC",
        text,
    )

    text = ZERO_WIDTH.sub(
        "",
        text,
    )

    for bad, good in MOJIBAKE.items():
        text = text.replace(
            bad,
            good,
        )

    text = text.replace(
        "\ufeff",
        "",
    )

    return text.strip()
