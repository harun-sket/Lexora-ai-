from __future__ import annotations

import re
from typing import List

# Tamil Unicode block
TAMIL = r"\u0B80-\u0BFF"

# Words (Tamil + English + numbers) OR punctuation
TOKEN_PATTERN = re.compile(
    rf"[{TAMIL}A-Za-z0-9]+|[^\s{TAMIL}A-Za-z0-9]",
    re.UNICODE,
)


class TamilTokenizer:
    """
    Lightweight tokenizer for Lexora.

    Splits:
    - Tamil words
    - English words
    - Numbers
    - Punctuation
    """

    def tokenize(self, text: str) -> List[str]:
        if not text:
            return []

        return TOKEN_PATTERN.findall(text)


def tokenize(text: str) -> List[str]:
    return TamilTokenizer().tokenize(text)
