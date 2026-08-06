"""
Lexora AI
Control Character Cleaner
"""

import re


def remove_control_characters(text: str):

    return re.sub(
        r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]",
        "",
        text
    )
