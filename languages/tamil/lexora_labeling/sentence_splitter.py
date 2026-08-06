"""
Lexora AI

Sentence Splitter
"""

from indicnlp.tokenize import sentence_tokenize


def split_sentences(text: str):

    return sentence_tokenize.sentence_split(
        text,
        lang="ta"
    )
