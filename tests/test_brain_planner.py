from pathlib import Path
from pprint import pprint

from languages.common.brain.quality_analyzer import analyze_text
from languages.common.brain.planner import create_plan

INPUT_FILE = "tests/data/quality_sample.txt"

text = Path(INPUT_FILE).read_text(encoding="utf-8")

report = analyze_text(text)
plan = create_plan(report)

print("========== QUALITY REPORT ==========")
pprint(report)

print("\n========== EXECUTION PLAN ==========")
for step in plan:
    print("->", step)
