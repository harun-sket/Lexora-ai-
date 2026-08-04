"""
Lexora AI
Tamil Text Normalizer v0.1
"""

import re


def normalize_tamil_text(text):

    # Remove spaces between Tamil word parts
    text = re.sub(
        r"([\u0B80-\u0BFF])\s+([\u0B80-\u0BFF])",
        r"\1\2",
        text
    )

    # Clean multiple spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()
