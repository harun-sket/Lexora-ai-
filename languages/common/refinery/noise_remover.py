"""
Lexora AI

Noise Remover

Removes OCR/text noise while preserving meaningful content.
"""

import re

# Remove long runs of symbols
_SYMBOL_NOISE = re.compile(r"[@#%&*_=+~^`|<>]{3,}")

# Remove emoji spam (2 or more)
_EMOJI_SPAM = re.compile(
    r"([\U0001F300-\U0001FAFF\U00002600-\U000027BF])\1+"
)

# Collapse repeated punctuation
_REPEAT_PUNCT = re.compile(r"([!?.,;:])\1{2,}")


def remove_noise(text: str) -> str:
    """Remove obvious visual noise."""

    # Remove symbol spam
    text = _SYMBOL_NOISE.sub("", text)

    # Remove repeated emojis
    text = _EMOJI_SPAM.sub("", text)

    # !!!!!! -> !
    text = _REPEAT_PUNCT.sub(r"\1", text)

    # Remove empty lines left behind
    lines = [line.rstrip() for line in text.splitlines()]
    lines = [line for line in lines if line.strip()]

    return "\n".join(lines)
