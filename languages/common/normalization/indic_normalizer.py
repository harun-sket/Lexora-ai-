"""
Lexora Indic Text Normalization

Wrapper around Indic NLP Library.

Responsibilities:
- Unicode normalization
- Canonical Indic normalization
- Language-aware normalization

This module does NOT decide when to run.
The Rule Engine decides that.
"""

from __future__ import annotations

from indicnlp.normalize.indic_normalize import IndicNormalizerFactory


_FACTORY = IndicNormalizerFactory()

_CACHE: dict[str, object] = {}


def _get_normalizer(language: str):
    """
    Lazily create and cache normalizers.
    """

    if language not in _CACHE:
        _CACHE[language] = _FACTORY.get_normalizer(language)

    return _CACHE[language]


def normalize_text(
    text: str,
    language: str = "ta",
) -> str:
    """
    Normalize Indic text.

    Parameters
    ----------
    text:
        Raw text.

    language:
        ISO language code.
        Example:
            ta
            hi
            ml
            te
            kn
            bn
    """

    normalizer = _get_normalizer(language)

    return normalizer.normalize(text)
