from __future__ import annotations

from languages.tamil.normalize import normalize_text
from languages.tamil.tokenize import tokenize
from languages.tamil.token import create_token


class TamilPipeline:
    """
    Lexora Language Intelligence Pipeline

    Raw Language
        ↓
    Normalize
        ↓
    Tokenize
        ↓
    Language Objects
    """

    def process(self, text: str) -> dict:

        normalized = normalize_text(text)

        tokens = tokenize(normalized)

        language_objects = [
            create_token(token)
            for token in tokens
        ]

        return {
            "original": text,
            "normalized": normalized,
            "objects": language_objects,
        }


_pipeline = TamilPipeline()


def process(text: str) -> dict:
    return _pipeline.process(text)


__all__ = [
    "TamilPipeline",
    "process",
]
