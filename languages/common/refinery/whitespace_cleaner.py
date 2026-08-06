"""
Lexora AI

Whitespace Cleaner

Removes:
- Multiple spaces
- Trailing spaces
- Empty lines
- Mixed line endings
"""

import re


def clean_whitespace(text: str) -> str:
    if not text:
        return ""

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    cleaned_lines = []

    for line in text.split("\n"):
        # Collapse multiple spaces/tabs
        line = re.sub(r"[ \t]+", " ", line)

        # Remove leading/trailing whitespace
        line = line.strip()

        cleaned_lines.append(line)

    # Remove repeated blank lines
    result = "\n".join(cleaned_lines)
    result = re.sub(r"\n{3,}", "\n\n", result)

    return result.strip()
