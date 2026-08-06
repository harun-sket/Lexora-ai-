"""
Lexora Broken Word Joiner

Repairs words that OCR splits across lines.

Example:

செயற்
கை

↓

செயற்கை
"""

import re


def join_broken_words(text: str) -> str:
    lines = text.splitlines()

    result = []
    i = 0

    while i < len(lines):
        current = lines[i].strip()

        if i + 1 < len(lines):
            nxt = lines[i + 1].strip()

            # Join only if BOTH look like word fragments
            if (
                current
                and nxt
                and " " not in current
                and " " not in nxt
                and re.search(r"[^\W\d_]", current)
                and re.search(r"[^\W\d_]", nxt)
            ):
                result.append(current + nxt)
                i += 2
                continue

        result.append(current)
        i += 1

    return "\n".join(result)
