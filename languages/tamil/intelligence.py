from __future__ import annotations


class TamilIntelligenceEngine:
    """
    Unified Lexora Tamil intelligence engine.

    Modules are imported lazily so the integration layer
    does not create circular package imports.
    """

    def analyze_token(self, token: str) -> dict[str, object]:
        from languages.tamil.ner import analyze as analyze_ner
        from languages.tamil.pos import tag as pos_tag

        ner_result = analyze_ner(token)

        return {
            "text": token,
            "known": ner_result["known"],
            "frequency": ner_result["frequency"],
            "pos": pos_tag(token),
            "entity": ner_result["entity"],
        }

    def process(self, text: str) -> dict[str, object]:
        from languages.tamil.tokenize import tokenize

        tokens = tokenize(text)

        return {
            "original": text,
            "tokens": tokens,
            "analysis": [
                self.analyze_token(token)
                for token in tokens
            ],
        }


_engine = TamilIntelligenceEngine()


def process(text: str) -> dict[str, object]:
    return _engine.process(text)


__all__ = [
    "TamilIntelligenceEngine",
    "process",
]
