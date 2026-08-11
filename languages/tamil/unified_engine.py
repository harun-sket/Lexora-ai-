from __future__ import annotations

from typing import Any

from languages.tamil.tokenize import tokenize
from languages.tamil.pos import tag as pos_tag
from languages.tamil.ner import analyze as ner_analyze
from languages.tamil.frequency import lookup


ENGINE_NAME = "lexora-tamil"
ENGINE_VERSION = "1.0"


class TamilUnifiedEngine:

    def __init__(self) -> None:
        self._tokenize = tokenize
        self._pos_tag = pos_tag
        self._ner_analyze = ner_analyze

    def analyze_token(
        self,
        token: str,
    ) -> dict[str, object]:

        frequency = lookup(token)

        pos = self._pos_tag(token)

        ner = self._ner_analyze(token)

        return {
            "text": token,
            "normalized": token,
            "corrected": token,
            "lemma": token,
            "known": frequency > 0,
            "frequency": frequency,
            "pos": pos,
            "entity": ner.get("entity", "NONE"),
            "morphology": None,
        }

    def process(
        self,
        text: str,
    ) -> dict[str, object]:

        if not isinstance(text, str):
            raise TypeError("text must be a string")

        tokens = self._tokenize(text)

        return {
            "engine": ENGINE_NAME,
            "version": ENGINE_VERSION,
            "original": text,
            "tokens": tokens,
            "analysis": [
                self.analyze_token(token)
                for token in tokens
            ],
        }


_engine = TamilUnifiedEngine()


def process(text: str) -> dict[str, object]:
    return _engine.process(text)


__all__ = [
    "ENGINE_NAME",
    "ENGINE_VERSION",
    "TamilUnifiedEngine",
    "process",
]
