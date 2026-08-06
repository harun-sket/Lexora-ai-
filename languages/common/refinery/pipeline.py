"""
Lexora Common Refinery Pipeline
"""

from languages.common.refinery.whitespace_cleaner import clean_whitespace
from languages.common.refinery.noise_remover import remove_noise
from languages.common.refinery.duplicate_line_remover import remove_duplicate_lines
from languages.common.refinery.broken_word_joiner import join_broken_words


def refine_text(text: str) -> str:
    text = clean_whitespace(text)
    text = remove_noise(text)
    text = remove_duplicate_lines(text)
    text = join_broken_words(text)

    return text
