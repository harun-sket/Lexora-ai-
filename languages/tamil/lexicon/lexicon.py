from __future__ import annotations

from dataclasses import dataclass

from languages.tamil.resources import load_frequency_dictionary


@dataclass(frozen=True)
class LexiconEntry:
    word: str
    frequency: int


class TamilLexicon:
    """
    Lexora Tamil Lexicon

    Shared lexical resource for every NLP module.
    """

    def __init__(self):
        self._dictionary = load_frequency_dictionary()

    def exists(self, word: str) -> bool:
        return word in self._dictionary

    def frequency(self, word: str) -> int:
        return self._dictionary.get(word, 0)

    def lookup(self, word: str) -> LexiconEntry | None:

        if word not in self._dictionary:
            return None

        return LexiconEntry(
            word=word,
            frequency=self._dictionary[word],
        )

    def vocabulary_size(self) -> int:
        return len(self._dictionary)

    def most_common(self, n: int = 20) -> list[LexiconEntry]:

        words = sorted(
            self._dictionary.items(),
            key=lambda x: x[1],
            reverse=True,
        )[:n]

        return [
            LexiconEntry(word=w, frequency=f)
            for w, f in words
        ]


_lexicon = TamilLexicon()


def exists(word: str) -> bool:
    return _lexicon.exists(word)


def frequency(word: str) -> int:
    return _lexicon.frequency(word)


def lookup(word: str):
    return _lexicon.lookup(word)


def vocabulary_size() -> int:
    return _lexicon.vocabulary_size()


def most_common(n: int = 20):
    return _lexicon.most_common(n)


__all__ = [
    "LexiconEntry",
    "TamilLexicon",
    "exists",
    "frequency",
    "lookup",
    "vocabulary_size",
    "most_common",
]
