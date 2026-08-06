from pathlib import Path
from pprint import pprint

from languages.common.brain.quality_analyzer import analyze_text

INPUT_FILE = "tests/data/quality_sample.txt"

text = Path(INPUT_FILE).read_text(encoding="utf-8")

report = analyze_text(text)

print("========== QUALITY REPORT ==========")
pprint(report)
