from __future__ import annotations

from dataclasses import dataclass, field
import re

from languages.tamil.lexicon import (
    exists,
    frequency,
)

from languages.tamil.spell.symspell_engine import correct_word
from languages.tamil.lemma import lemmatize
from languages.tamil.morphology import analyze


@dataclass
class TamilToken:
    """
    Lexora Language Object

    Every module enriches this object.
    """

    # Original
    text: str

    # Classification
    token_type: str = "UNKNOWN"

    # Spell Intelligence
    corrected: str | None = None
    changed: bool = False
    edit_distance: int = 0

    # Lexicon
    known: bool = False
    frequency: int = 0

    # Linguistics
    lemma: str | None = None
    root: str | None = None
    suffixes: list[str] = field(default_factory=list)

    # POS
    pos: str | None = None

    # Named Entity
    entity: str | None = None

    def classify(self):

        if self.text.isdigit():
            self.token_type = "NUMBER"
            return

        if re.fullmatch(r"[A-Za-z]+", self.text):
            self.token_type = "LATIN"
            return

        if re.fullmatch(r"[.,!?;:()\"'…\-]+", self.text):
            self.token_type = "PUNCTUATION"
            return

        if re.search(r"[\u0B80-\u0BFF]", self.text):
            self.token_type = "TAMIL"
            return

        self.token_type = "UNKNOWN"

    def enrich(self):

        self.classify()

        # Skip non-Tamil tokens
        if self.token_type != "TAMIL":
            self.corrected = self.text
            return self

        # Lexicon
        self.known = exists(self.text)

        if self.known:

            self.corrected = self.text
            self.frequency = frequency(self.text)

        else:

            suggestion = correct_word(self.text)

            if suggestion:

                self.corrected = suggestion["corrected"]
                self.changed = suggestion["changed"]
                self.edit_distance = suggestion["distance"]

                self.known = exists(self.corrected)

                if self.known:
                    self.frequency = frequency(self.corrected)

            else:

                self.corrected = self.text

        # Lemma
        lemma_result = lemmatize(self.corrected)

        self.lemma = lemma_result.lemma

        # Morphology
        morph = analyze(self.corrected)

        self.root = morph.root
        self.suffixes = morph.suffixes

        return self

    def to_dict(self):

        return {
            "text": self.text,
            "token_type": self.token_type,
            "corrected": self.corrected,
            "changed": self.changed,
            "edit_distance": self.edit_distance,
            "known": self.known,
            "frequency": self.frequency,
            "lemma": self.lemma,
            "root": self.root,
            "suffixes": self.suffixes,
            "pos": self.pos,
            "entity": self.entity,
        }


def create_token(word: str) -> TamilToken:
    return TamilToken(word).enrich()


__all__ = [
    "TamilToken",
    "create_token",
]
