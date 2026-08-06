from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from symspellpy import SymSpell, Verbosity


class TamilSymSpell:
    """
    Tamil SymSpell wrapper for Lexora.

    Loads a pre-built frequency dictionary generated from wordfreq
    and provides fast spelling correction + suggestions.
    """

    def __init__(
        self,
        dictionary_path: str | Path,
        max_dictionary_edit_distance: int = 2,
        prefix_length: int = 7,
    ):
        self.dictionary_path = Path(dictionary_path)

        self.symspell = SymSpell(
            max_dictionary_edit_distance=max_dictionary_edit_distance,
            prefix_length=prefix_length,
        )

        loaded = self.symspell.load_dictionary(
            str(self.dictionary_path),
            term_index=0,
            count_index=1,
        )

        if not loaded:
            raise FileNotFoundError(
                f"Could not load dictionary: {self.dictionary_path}"
            )

    def lookup(
        self,
        word: str,
        max_edit_distance: int = 2,
    ) -> dict | None:
        """
        Return the best spelling correction.
        """

        suggestions = self.symspell.lookup(
            word,
            Verbosity.TOP,
            max_edit_distance=max_edit_distance,
        )

        if not suggestions:
            return None

        best = suggestions[0]

        return {
            "original": word,
            "corrected": best.term,
            "distance": best.distance,
            "frequency": best.count,
            "changed": best.term != word,
        }

    def lookup_all(
        self,
        word: str,
        max_edit_distance: int = 2,
    ) -> list[dict]:
        """
        Return all spelling suggestions.
        """

        suggestions = self.symspell.lookup(
            word,
            Verbosity.ALL,
            max_edit_distance=max_edit_distance,
        )

        return [
            {
                "term": s.term,
                "distance": s.distance,
                "frequency": s.count,
            }
            for s in suggestions
        ]


@lru_cache(maxsize=1)
def get_symspell() -> TamilSymSpell:
    """
    Singleton loader.
    """

    dictionary = (
        Path(__file__).resolve().parent
        / "data"
        / "ta_frequency_dictionary.txt"
    )

    return TamilSymSpell(dictionary)


def correct_word(
    word: str,
    max_edit_distance: int = 2,
):
    """
    Return the best correction.
    """

    return get_symspell().lookup(
        word,
        max_edit_distance=max_edit_distance,
    )


def suggest(
    word: str,
    max_edit_distance: int = 2,
):
    """
    Return all suggestions.
    """

    return get_symspell().lookup_all(
        word,
        max_edit_distance=max_edit_distance,
    )


__all__ = [
    "TamilSymSpell",
    "get_symspell",
    "correct_word",
    "suggest",
]
