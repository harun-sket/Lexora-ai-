from __future__ import annotations

from functools import lru_cache
from pathlib import Path


# Use Lexora's existing frequency dictionary.
FREQUENCY_DATA = (
    Path(__file__).resolve().parent.parent
    / "resources"
    / "data"
    / "ta_frequency_dictionary.txt"
)


@lru_cache(maxsize=1)
def load_frequency_dictionary() -> dict[str, int]:
    """
    Load Lexora's existing Tamil frequency dictionary.

    Format:
        word frequency
    """
    dictionary: dict[str, int] = {}

    if not FREQUENCY_DATA.exists():
        return dictionary

    with FREQUENCY_DATA.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.rsplit(maxsplit=1)

            if len(parts) != 2:
                continue

            word, frequency = parts

            try:
                dictionary[word] = int(frequency)
            except ValueError:
                continue

    return dictionary


# Small entity-specific knowledge layer.
# Frequency tells us whether a word is known/common.
# This mapping tells us what kind of entity it is.
ENTITY_TYPES: dict[str, str] = {
    "இந்தியா": "LOCATION",
    "தமிழ்நாடு": "LOCATION",
    "சென்னை": "LOCATION",
    "மதுரை": "LOCATION",
    "கோயம்புத்தூர்": "LOCATION",

    "இந்திய அரசு": "ORGANIZATION",
    "தமிழ்நாடு அரசு": "ORGANIZATION",
}


class TamilNER:
    """
    Lightweight Tamil Named Entity Recognizer.

    Uses Lexora's frequency dictionary as the vocabulary layer
    and a separate entity mapping for entity classification.
    """

    def is_known(self, word: str) -> bool:
        return word in load_frequency_dictionary()

    def frequency(self, word: str) -> int:
        return load_frequency_dictionary().get(word, 0)

    def recognize(self, word: str) -> str:
        if not word:
            return "NONE"

        # Don't classify completely unknown vocabulary as an entity.
        if not self.is_known(word):
            return "NONE"

        return ENTITY_TYPES.get(word, "NONE")

    def analyze(self, word: str) -> dict[str, object]:
        return {
            "text": word,
            "known": self.is_known(word),
            "frequency": self.frequency(word),
            "entity": self.recognize(word),
        }

    def recognize_tokens(
        self,
        tokens: list[str],
    ) -> list[dict[str, object]]:
        return [
            self.analyze(token)
            for token in tokens
        ]


_ner = TamilNER()


def recognize(word: str) -> str:
    return _ner.recognize(word)


def analyze(word: str) -> dict[str, object]:
    return _ner.analyze(word)


def recognize_tokens(
    tokens: list[str],
) -> list[dict[str, object]]:
    return _ner.recognize_tokens(tokens)


__all__ = [
    "TamilNER",
    "recognize",
    "analyze",
    "recognize_tokens",
]
