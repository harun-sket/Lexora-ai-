"""
Lexora Tamil Named Entity Recognition Package
"""

from .tagger import (
    TamilNER,
    analyze,
    recognize,
    recognize_tokens,
)

__all__ = [
    "TamilNER",
    "analyze",
    "recognize",
    "recognize_tokens",
]
