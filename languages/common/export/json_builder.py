"""
Lexora JSON Builder

Converts a Document into the official
Lexora JSON format.
"""

from __future__ import annotations

from dataclasses import asdict
import json

from languages.common.pipeline.document import Document


LEXORA_VERSION = "1.0.0"


def build(document: Document) -> dict:
    """
    Convert a Document into a JSON-ready dictionary.
    """

    return {
        "lexora_version": LEXORA_VERSION,
        "raw_text": document.raw_text,
        "normalized_text": document.normalized_text,
        "quality": document.quality,
        "plan": document.plan,
        "labels": document.labels,
        "actions": document.actions,
        "confidence": document.confidence,
        "metadata": document.metadata,
    }


def to_json(document: Document, indent: int = 4) -> str:
    """
    Serialize a Document to JSON.
    """

    return json.dumps(
        build(document),
        ensure_ascii=False,
        indent=indent,
    )
