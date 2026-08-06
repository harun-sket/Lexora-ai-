"""
Lexora Production Document

Every module reads from and writes to this object.

This is the heart of the production pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Document:
    raw_text: str

    normalized_text: str = ""

    quality: dict = field(default_factory=dict)

    plan: list = field(default_factory=list)

    labels: dict = field(default_factory=dict)

    actions: list = field(default_factory=list)

    confidence: dict = field(default_factory=dict)

    metadata: dict = field(default_factory=dict)
