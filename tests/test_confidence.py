from pathlib import Path
from pprint import pprint

from languages.common.quality.quality_analyzer import analyze_quality
from languages.common.confidence.confidence_scorer import score

text = Path(
    "tests/data/confidence_input.txt"
).read_text(encoding="utf-8")

quality = analyze_quality(text)

confidence = score(quality)

print("========== QUALITY ==========")
pprint(quality)

print("\n========== CONFIDENCE ==========")
pprint(confidence)
