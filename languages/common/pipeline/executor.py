"""
Lexora Production Executor

Coordinates the complete language intelligence pipeline.
"""

from __future__ import annotations

from languages.common.pipeline.document import Document

from languages.common.quality.quality_analyzer import analyze_quality
from languages.common.brain.planner import create_plan
from languages.common.labeling.labeler import label_text
from languages.common.rules.engine import decide
from languages.common.normalization.indic_normalizer import normalize_text
from languages.common.confidence.confidence_scorer import score
from languages.common.export.json_builder import build


INDIC_LANGUAGES = {
    "ta",
    "hi",
    "ml",
    "te",
    "kn",
    "bn",
    "gu",
    "mr",
    "pa",
    "or",
    "as",
}


def _normalize_language(language: str) -> str:
    """
    Convert language codes into ISO-639-1 lowercase.
    """

    if not language:
        return "ta"

    mapping = {
        "TAMIL": "ta",
        "TA": "ta",
        "ENGLISH": "en",
        "EN": "en",
        "HINDI": "hi",
        "HI": "hi",
        "TELUGU": "te",
        "TE": "te",
        "MALAYALAM": "ml",
        "ML": "ml",
        "KANNADA": "kn",
        "KN": "kn",
        "BENGALI": "bn",
        "BN": "bn",
        "GUJARATI": "gu",
        "GU": "gu",
        "MARATHI": "mr",
        "MR": "mr",
        "PUNJABI": "pa",
        "PA": "pa",
        "ODIA": "or",
        "ORIYA": "or",
        "OR": "or",
        "ASSAMESE": "as",
        "AS": "as",
    }

    language = language.strip().upper()

    return mapping.get(language, language.lower())


def run_pipeline(text: str) -> dict:
    """
    Execute the complete Lexora pipeline.
    """

    document = Document(raw_text=text)

    # --------------------------
    # Quality
    # --------------------------

    document.quality = analyze_quality(document.raw_text)

    # --------------------------
    # Brain
    # --------------------------

    document.plan = create_plan(document.quality)

    # --------------------------
    # Labeling
    # --------------------------

    document.labels = label_text(document.raw_text)

    # --------------------------
    # Rules
    # --------------------------

    decision = decide(document.labels)

    document.actions = decision.get("actions", [])

    # --------------------------
    # Language
    # --------------------------

    language = "ta"

    detected = document.labels.get("languages", [])

    if detected:
        language = _normalize_language(detected[0])

    # --------------------------
    # Indic Normalization
    # --------------------------

    if (
        "run_indic_normalization" in document.actions
        and language in INDIC_LANGUAGES
    ):
        document.normalized_text = normalize_text(
            document.raw_text,
            language,
        )
    else:
        document.normalized_text = document.raw_text

    # --------------------------
    # Confidence
    # --------------------------

    document.confidence = score(document.quality)

    # --------------------------
    # Metadata
    # --------------------------

    document.metadata["language"] = language

    # --------------------------
    # Export
    # --------------------------

    return build(document)

