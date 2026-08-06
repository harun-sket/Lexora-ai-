"""
Lexora Confidence Scorer

Purpose
-------
Estimate confidence based on the quality analysis.

This module does not modify text.
It only estimates confidence for downstream systems.
"""

from __future__ import annotations


def score(quality: dict) -> dict:
    quality_score = quality.get("quality_score", 0)

    confidence = quality_score

    penalties = []

    if quality.get("replacement_characters", 0):
        penalties.append("unicode_noise")

    if quality.get("multiple_spaces", 0):
        penalties.append("whitespace_noise")

    if quality.get("blank_lines", 0):
        penalties.append("blank_lines")

    level = "high"

    if confidence < 85:
        level = "medium"

    if confidence < 60:
        level = "low"

    return {
        "score": confidence,
        "level": level,
        "penalties": penalties,
    }
