"""
Lexora AI
Tamil OCR Correction Engine v0.1

Rule-based correction for common OCR mistakes.
"""

import re


# Common OCR corrections
CORRECTIONS = {
    "தம் ழ்": "தமிழ்",
    "வணக் கம்": "வணக்கம்",
    "லக்சோரா": "லெக்சோரா",
}


def correct_text(text: str) -> str:
    """
    Apply rule-based OCR corrections.
    """

    for wrong, correct in CORRECTIONS.items():
        text = text.replace(
            wrong,
            correct
        )

    # Remove unnecessary spaces between Tamil letters
    text = re.sub(
        r"([\u0B80-\u0BFF])\s+([\u0B80-\u0BFF])",
        r"\1\2",
        text
    )

    return text.strip()
