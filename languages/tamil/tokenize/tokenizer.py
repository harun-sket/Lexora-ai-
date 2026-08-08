from __future__ import annotations

import re
from typing import List

# Tamil Unicode block
TAMIL_BLOCK = "\u0B80-\u0BFF"

# Token pattern:
# - Tamil words
# - English words
# - Numbers
# - Individual punctuation
TOKEN_PATTERN = re.compile(
    rf"[{TAMIL_BLOCK}A-Za-z0-9]+|[^\s{TAMIL_BLOCK}A-Za-z0-9]",
    re.UNICODE,
)


class TamilTokenizer:
    """
    Lexora Tokenizer

    Responsibilities
    ----------------
    - Split Tamil words
    - Split English words
    - Split numbers
    - Preserve punctuation

    Does NOT:
    - Normalize
    - Spell-correct
    - Lemmatize
    - POS tag
    """

    def tokenize(self, text: str) -> List[str]:
        if not text:
            return []

        return TOKEN_PATTERN.findall(text)


_tokenizer = TamilTokenizer()


def tokenize(text: str) -> List[str]:
    return _tokenizer.tokenize(text)


__all__ = [
    "TamilTokenizer",
    "tokenize",
]
