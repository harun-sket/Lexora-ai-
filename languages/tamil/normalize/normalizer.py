"""
Lexora Tamil Normalizer

Responsibilities
----------------
- Unicode NFC normalization
- Remove zero-width characters
- Normalize whitespace
- Normalize Tamil punctuation
- Preserve Tamil characters
"""

from __future__ import annotations

import re
import unicodedata

__all__ = [
    "TamilNormalizer",
    "normalize_text",
]


class TamilNormalizer:
    """Unicode-aware Tamil text normalizer."""

    _ZERO_WIDTH_RE = re.compile(r"[\u200B\u200C\u200D\uFEFF]")
    _WHITESPACE_RE = re.compile(r"\s+")

    _PUNCT_TRANSLATION = str.maketrans({
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "–": "-",
        "—": "-",
        "…": "...",
    })

    def normalize(self, text: str) -> str:
        """
        Normalize Tamil text.

        Parameters
        ----------
        text : str
            Raw input string.

        Returns
        -------
        str
            Clean normalized text.
        """
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        # Unicode normalization
        text = unicodedata.normalize("NFC", text)

        # Remove zero-width characters
        text = self._ZERO_WIDTH_RE.sub("", text)

        # Normalize punctuation
        text = text.translate(self._PUNCT_TRANSLATION)

        # Normalize whitespace
        text = self._WHITESPACE_RE.sub(" ", text)

        return text.strip()


_normalizer = TamilNormalizer()


def normalize_text(text: str) -> str:
    """
    Convenience function.

    Example
    -------
    >>> normalize_text("  தமிழ்   மொழி ")
    'தமிழ் மொழி'
    """
    return _normalizer.normalize(text)


if __name__ == "__main__":
    examples = [
        "  தமிழ்   மொழி  ",
        "வணக்கம்\u200B உலகம்",
        "“தமிழ்”",
        "தமிழ்…",
    ]

    for example in examples:
        print("RAW :", repr(example))
        print("NORM:", repr(normalize_text(example)))
        print("-" * 40)
