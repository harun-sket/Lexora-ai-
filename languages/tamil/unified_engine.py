from __future__ import annotations

from typing import Any


ENGINE_NAME = "lexora-tamil"
ENGINE_VERSION = "1.0"


class TamilUnifiedEngine:
    """
    Stable public contract for Lexora Tamil v1.0.

    Pipeline:

        raw text
            ↓
        tokenizer
            ↓
        frequency
            ↓
        POS
            ↓
        NER
            ↓
        spell correction
            ↓
        lemmatization
            ↓
        morphology
            ↓
        unified output
    """

    def __init__(self) -> None:
        from languages.tamil.ner import analyze as ner_analyze
        from languages.tamil.pos import tag as pos_tag
        from languages.tamil.tokenize import tokenize

        self._tokenize = tokenize
        self._ner_analyze = ner_analyze
        self._pos_tag = pos_tag

        self._spell_correct = self._load_optional(
            "languages.tamil.spell",
            "correct",
        )

        self._lemmatize = self._load_optional(
            "languages.tamil.lemma",
            "lemmatize",
        )

        self._morph_analyze = self._load_optional(
            "languages.tamil.morphology",
            "analyze",
        )

    @staticmethod
    def _load_optional(
        module_name: str,
        function_name: str,
    ) -> Any | None:
        try:
            module = __import__(
                module_name,
                fromlist=[function_name],
            )

            return getattr(module, function_name, None)

        except (ImportError, AttributeError):
            return None

    @staticmethod
    def _safe_call(
        function: Any | None,
        value: str,
        default: Any = None,
    ) -> Any:
        if function is None:
            return default

        try:
            return function(value)

        except (
            TypeError,
            ValueError,
            KeyError,
        ):
            return default

    def analyze_token(
        self,
        token: str,
    ) -> dict[str, object]:

        ner = self._ner_analyze(token)

        corrected = self._safe_call(
            self._spell_correct,
            token,
            token,
        )

        # Always keep the public contract string-safe.
        if not isinstance(corrected, str):
            corrected = token

        lemma = self._safe_call(
            self._lemmatize,
            corrected,
            corrected,
        )

        # If the lemmatizer is unavailable or returns
        # an unexpected value, preserve the corrected token.
        if not isinstance(lemma, str):
            lemma = corrected

        morphology = self._safe_call(
            self._morph_analyze,
            corrected,
            None,
        )

        return {
            "text": token,
            "normalized": token,
            "corrected": corrected,
            "lemma": lemma,
            "known": bool(
                ner.get("known", False)
            ),
            "frequency": int(
                ner.get("frequency", 0)
            ),
            "pos": self._pos_tag(token),
            "entity": ner.get(
                "entity",
                "NONE",
            ),
            "morphology": morphology,
        }

    def process(
        self,
        text: str,
    ) -> dict[str, object]:

        if not isinstance(text, str):
            raise TypeError(
                "text must be a string"
            )

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


def process(
    text: str,
) -> dict[str, object]:
    """
    Process Tamil text using Lexora's
    stable v1.0 contract.
    """
    return _engine.process(text)


__all__ = [
    "ENGINE_NAME",
    "ENGINE_VERSION",
    "TamilUnifiedEngine",
    "process",
]
