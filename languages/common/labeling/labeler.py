"""
Lexora Indic NLP Labeler

Purpose
-------
Produces structured labels from raw text.

This is the ONLY module that directly talks to the
Indic NLP Library.

All other Lexora modules consume the returned JSON.
"""

from __future__ import annotations

import re

from indicnlp.tokenize import indic_tokenize


EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
URL_RE = re.compile(r"https?://\S+|www\.\S+")
PHONE_RE = re.compile(r"\+?\d[\d\s\-]{7,}")
NUMBER_RE = re.compile(r"\d+")

TAMIL_RE = re.compile(r"[\u0B80-\u0BFF]")
ENGLISH_RE = re.compile(r"[A-Za-z]")


def label_text(text: str) -> dict:
    """
    Analyze text and return structured labels.
    """

    tokens = indic_tokenize.trivial_tokenize(text)

    labels = {
        "tokens": tokens,
        "token_count": len(tokens),
        "languages": [],
        "contains_tamil": False,
        "contains_english": False,
        "contains_numbers": False,
        "contains_email": False,
        "contains_url": False,
        "contains_phone": False,
    }

    if TAMIL_RE.search(text):
        labels["contains_tamil"] = True
        labels["languages"].append("ta")

    if ENGLISH_RE.search(text):
        labels["contains_english"] = True
        labels["languages"].append("en")

    if NUMBER_RE.search(text):
        labels["contains_numbers"] = True

    if EMAIL_RE.search(text):
        labels["contains_email"] = True

    if URL_RE.search(text):
        labels["contains_url"] = True

    if PHONE_RE.search(text):
        labels["contains_phone"] = True

    labels["languages"] = sorted(set(labels["languages"]))

    return labels
