from __future__ import annotations

from languages.tamil.normalize import normalize_text
from languages.tamil.tokenize import tokenize
from languages.tamil.spell.symspell_engine import correct_word


class TamilPipeline:
    """
    Complete Tamil NLP Pipeline.
    """

    def process(self, text: str) -> dict:
        normalized = normalize_text(text)

        tokens = tokenize(normalized)

        corrected_tokens = []
        corrections = []

        for token in tokens:
            result = correct_word(token)

            if result is None:
                corrected_tokens.append(token)
                continue

            corrected_tokens.append(result["corrected"])

            if result["changed"]:
                corrections.append(result)

        return {
            "original": text,
            "normalized": normalized,
            "tokens": tokens,
            "corrected_tokens": corrected_tokens,
            "corrected_text": " ".join(corrected_tokens),
            "corrections": corrections,
        }


_pipeline = TamilPipeline()


def process(text: str) -> dict:
    return _pipeline.process(text)


__all__ = [
    "TamilPipeline",
    "process",
]
