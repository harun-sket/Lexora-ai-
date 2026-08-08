from __future__ import annotations

from functools import lru_cache
from pathlib import Path


POS_DATA = (
    Path(__file__).resolve().parent
    / "data"
    / "ta_pos_dictionary.txt"
)


@lru_cache(maxsize=1)
def load_pos_dictionary() -> dict[str, str]:
    dictionary: dict[str, str] = {}

    if not POS_DATA.exists():
        return dictionary

    with POS_DATA.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.split("\t")

            if len(parts) != 2:
                continue

            word, pos = parts

            dictionary[word] = pos

    return dictionary


class TamilPOSTagger:
    """
    Lightweight dictionary-based Tamil POS tagger.

    Unknown words return UNK.
    """

    def tag(self, word: str) -> str:
        if not word:
            return "UNK"

        return load_pos_dictionary().get(word, "UNK")

    def tag_tokens(self, tokens: list[str]) -> list[dict[str, str]]:
        return [
            {
                "text": token,
                "pos": self.tag(token),
            }
            for token in tokens
        ]


_tagger = TamilPOSTagger()


def tag(word: str) -> str:
    return _tagger.tag(word)


def tag_tokens(tokens: list[str]) -> list[dict[str, str]]:
    return _tagger.tag_tokens(tokens)


__all__ = [
    "TamilPOSTagger",
    "tag",
    "tag_tokens",
]
