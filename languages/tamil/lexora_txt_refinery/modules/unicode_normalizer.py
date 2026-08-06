"""
Lexora AI
Unicode Normalizer
"""

import unicodedata


def normalize_unicode(text: str):

    return unicodedata.normalize(
        "NFC",
        text
    )
