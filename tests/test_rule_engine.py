from pathlib import Path
from pprint import pprint

from languages.common.labeling.labeler import label_text
from languages.common.rules.engine import decide

text = Path("tests/data/rule_engine_input.txt").read_text(encoding="utf-8")

labels = label_text(text)

decision = decide(labels)

print("========== LABELS ==========")
pprint(labels)

print("\n========== DECISION ==========")
pprint(decision)
