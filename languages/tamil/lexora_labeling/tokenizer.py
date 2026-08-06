"""
Lexora AI

Indic NLP Tokenizer
"""

from indicnlp.tokenize import indic_tokenize


def tokenize(text: str):

    return indic_tokenize.trivial_tokenize(text)
