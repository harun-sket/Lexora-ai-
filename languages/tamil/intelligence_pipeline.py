from __future__ import annotations

from languages.tamil.normalize import normalize_text
from languages.tamil.tokenize import tokenize
from languages.tamil.token import create_token


class LanguageIntelligencePipeline:
    """
    Lexora Language Intelligence Pipeline v0.1

    Converts raw language into Language Objects.
    """

    def process(self, text: str):

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


_pipeline = LanguageIntelligencePipeline()


def process(text: str):
    return _pipeline.process(text)


__all__ = [
    "LanguageIntelligencePipeline",
    "process",
]
