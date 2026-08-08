from __future__ import annotations

from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=1)
def load_frequency_dictionary() -> dict[str, int]:
    """
    Load the Tamil frequency dictionary.

    Returns:
        dict[word] = frequency
    """

    dictionary = (
        Path(__file__).resolve().parent.parent
        / "spell"
        / "data"
        / "ta_frequency_dictionary.txt"
    )

    if not dictionary.exists():
        raise FileNotFoundError(
            f"Frequency dictionary not found:\n{dictionary}"
        )

    words: dict[str, int] = {}

    with dictionary.open(
        encoding="utf-8"
    ) as f:

        for line in f:

            line = line.strip()

            if not line:
                continue

            try:
                word, count = line.split()

                words[word] = int(count)

            except ValueError:
                continue

    return words


def word_exists(word: str) -> bool:
    """
    Check whether a word exists in the frequency dictionary.
    """
    return word in load_frequency_dictionary()


def frequency(word: str) -> int:
    """
    Return the frequency of a word.
    """
    return load_frequency_dictionary().get(word, 0)


__all__ = [
    "load_frequency_dictionary",
    "word_exists",
    "frequency",
]
