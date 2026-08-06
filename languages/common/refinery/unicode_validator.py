"""
Lexora Unicode Validator

Purpose:
- Detect mojibake
- Detect replacement characters
- Detect broken Unicode
- Produce quality statistics
"""

from collections import Counter

REPLACEMENT = "\uFFFD"

# Characters frequently seen in mojibake
SUSPICIOUS = set("ÃÂÐÑØÕŒ¤¦¨¬±²³µ¶·¸¼½¾")


def unicode_report(text: str) -> dict:
    total = len(text)

    replacement = text.count(REPLACEMENT)

    suspicious = sum(
        1
        for c in text
        if c in SUSPICIOUS
    )

    control = sum(
        1
        for c in text
        if ord(c) < 32 and c not in ("\n", "\t", "\r")
    )

    return {
        "characters": total,
        "replacement_characters": replacement,
        "suspicious_unicode": suspicious,
        "control_characters": control,
        "unicode_ok": (
            replacement == 0
            and suspicious == 0
            and control == 0
        )
    }


def has_unicode_errors(text: str) -> bool:
    report = unicode_report(text)
    return not report["unicode_ok"]


if __name__ == "__main__":
    sample = "வணக்கம் ÃÃ� தமிழ்"

    print(unicode_report(sample))
