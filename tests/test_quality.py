from pathlib import Path
from pprint import pprint

from languages.common.quality.quality_analyzer import analyze_quality

text = Path(
    "tests/data/quality_input.txt"
).read_text(encoding="utf-8")

report = analyze_quality(text)

print("========== QUALITY REPORT ==========")
pprint(report)
