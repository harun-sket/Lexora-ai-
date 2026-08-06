"""
Lexora AI

Label Models
"""

from dataclasses import dataclass


@dataclass
class TokenLabel:

    token: str

    label: str

    language: str
