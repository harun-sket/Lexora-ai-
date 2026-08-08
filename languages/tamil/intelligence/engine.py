from __future__ import annotations

from languages.tamil.token import TamilToken


class TamilIntelligenceEngine:
    """
    Lexora Intelligence Engine.

    Responsible for enriching a TamilToken by
    executing every language intelligence stage.
    """

    def enrich(self, token: TamilToken) -> TamilToken:
        return token.enrich()


_engine = TamilIntelligenceEngine()


def enrich(token: TamilToken) -> TamilToken:
    return _engine.enrich(token)


__all__ = [
    "TamilIntelligenceEngine",
    "enrich",
]
