"""
Lexora AI
Language Validator
"""

import re


def analyze_language(text: str):

    tamil = len(
        re.findall(
            r"[\u0B80-\u0BFF]",
            text
        )
    )

    english = len(
        re.findall(
            r"[A-Za-z]",
            text
        )
    )

    digits = len(
        re.findall(
            r"\d",
            text
        )
    )

    total = max(
        tamil + english + digits,
        1
    )

    return {

        "tamil_percent":
            round(
                tamil / total * 100,
                2
            ),

        "english_percent":
            round(
                english / total * 100,
                2
            ),

        "digit_percent":
            round(
                digits / total * 100,
                2
            )

    }
