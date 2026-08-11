from __future__ import annotations

from pathlib import Path


_DICTIONARY = (
    Path(__file__).resolve().parent
    / "data"
    / "ta_frequency_dictionary.txt"
)


def _load_dictionary() -> dict[str, int]:
    frequencies: dict[str, int] = {}

    if not _DICTIONARY.exists():
        return frequencies

    with _DICTIONARY.open(
        "r",
        encoding="utf-8",
    ) as file:

        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.rsplit(maxsplit=1)

            if len(parts) != 2:
                continue

            word, frequency = parts

            try:
                frequencies[word] = int(frequency)
            except ValueError:
                continue

    return frequencies


FREQUENCY_DICTIONARY = _load_dictionary()


def lookup(word: str) -> int:
    return FREQUENCY_DICTIONARY.get(
        word,
        0,
    )


__all__ = [
    "FREQUENCY_DICTIONARY",
    "lookup",
]
