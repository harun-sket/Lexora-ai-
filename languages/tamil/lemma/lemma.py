from __future__ import annotations

from dataclasses import dataclass

from languages.tamil.morphology import analyze


@dataclass
class LemmaResult:
    """
    Canonical representation of a word.
    """
    word: str
    lemma: str


class TamilLemmatizer:
    """
    Lexora Tamil Lemmatizer v0.1

    Current:
        Uses morphology root.

    Future:
        - Dictionary lookup
        - Verb lemmatization
        - Irregular forms
    """

    def lemmatize(self, word: str) -> LemmaResult:
        morph = analyze(word)

        return LemmaResult(
            word=word,
            lemma=morph.root,
        )


_lemmatizer = TamilLemmatizer()


def lemmatize(word: str) -> LemmaResult:
    return _lemmatizer.lemmatize(word)


__all__ = [
    "LemmaResult",
    "TamilLemmatizer",
    "lemmatize",
]
