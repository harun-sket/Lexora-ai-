"""
Lexora Rule Engine

Consumes labels and decides what actions should be taken.

It NEVER edits text.

It only returns structured decisions.
"""

from __future__ import annotations


def decide(labels: dict) -> dict:
    actions = []

    if labels.get("contains_numbers"):
        actions.append("normalize_numbers")

    if labels.get("contains_email"):
        actions.append("preserve_email")

    if labels.get("contains_url"):
        actions.append("preserve_url")

    if labels.get("contains_phone"):
        actions.append("normalize_phone")

    if labels.get("contains_tamil"):
        actions.append("run_indic_normalization")

    if labels.get("contains_english"):
        actions.append("run_symspell_if_needed")

    return {
        "actions": actions,
        "action_count": len(actions),
    }
