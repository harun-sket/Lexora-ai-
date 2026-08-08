"""
Lexora Tamil POS Package
"""

from .tagger import (
    TamilPOSTagger,
    tag,
    tag_tokens,
)

__all__ = [
    "TamilPOSTagger",
    "tag",
    "tag_tokens",
]
