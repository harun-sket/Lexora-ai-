"""
Lexora Brain Planner

Decides which refinement modules should run based on
the quality analysis report.

This file contains NO text processing.
It only decides the execution plan.
"""

from __future__ import annotations


def create_plan(report: dict) -> list[str]:
    """
    Create an execution plan from a quality report.

    Parameters
    ----------
    report : dict
        Output from quality_analyzer.analyze_text()

    Returns
    -------
    list[str]
        Ordered list of module names.
    """

    plan: list[str] = []

    # Always validate Unicode first.
    plan.append("unicode_validator")

    # Normalize whitespace if needed.
    if report.get("whitespace_characters", 0) > 0:
        plan.append("whitespace_cleaner")

    # Remove noisy symbols.
    if report.get("noise_characters", 0) > 0:
        plan.append("noise_remover")

    # Remove duplicate lines.
    if report.get("duplicate_lines", 0) > 0:
        plan.append("duplicate_line_remover")

    # Future modules (disabled until implemented)
    #
    # if report.get("broken_words", 0):
    #     plan.append("broken_word_joiner")
    #
    # if report.get("needs_normalization", False):
    #     plan.append("indic_text_normalizer")
    #
    # if report.get("ocr_confidence", 100) < 95:
    #     plan.append("symspell")
    #
    # if report.get("paragraphs", 0) == 0:
    #     plan.append("paragraph_builder")

    return plan
