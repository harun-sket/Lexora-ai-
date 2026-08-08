from __future__ import annotations

from dataclasses import dataclass


# Common Tamil plural suffixes
PLURAL_SUFFIXES = [
    "க்கள்",
    "ங்கள்",
    "கள்",
]


@dataclass
class MorphAnalysis:
    word: str
    root: str
    suffixes: list[str]


class TamilMorphAnalyzer:
    """
    Lexora Tamil Morphological Analyzer v0.1

    Supports:
    - Basic plural suffix detection

    Future:
    - Case markers
    - Verb morphology
    - PNG features
    - Tense
    """

    def analyze(self, word: str) -> MorphAnalysis:

        for suffix in PLURAL_SUFFIXES:

            if word.endswith(suffix):

                root = word[:-len(suffix)]

                return MorphAnalysis(
                    word=word,
                    root=root,
                    suffixes=[suffix],
                )

        return MorphAnalysis(
            word=word,
            root=word,
            suffixes=[],
        )


_analyzer = TamilMorphAnalyzer()


def analyze(word: str):
    return _analyzer.analyze(word)


__all__ = [
    "MorphAnalysis",
    "TamilMorphAnalyzer",
    "analyze",
]
