"""
Lexora AI

Tamil Label Generator
"""

import re

from .labels import *

from .models import TokenLabel

from .tokenizer import tokenize


def generate_labels(text: str):

    output = []

    tokens = tokenize(text)

    for token in tokens:

        if token.isdigit():

            label = NUMBER

        elif re.fullmatch(r"[.,!?;:]", token):

            label = PUNCTUATION

        elif re.fullmatch(r"[^\w\s]+", token):

            label = SYMBOL

        else:

            label = WORD

        output.append(

            TokenLabel(

                token=token,

                label=label,

                language="ta"

            )

        )

    return output
