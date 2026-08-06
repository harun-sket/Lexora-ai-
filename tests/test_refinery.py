from pathlib import Path

from languages.common.refinery.pipeline import refine_text

INPUT_FILE = "storage/uploads/tamil_test.txt"

text = Path(INPUT_FILE).read_text(encoding="utf-8")

print("========== ORIGINAL ==========")
print(text)

print("\n========== REFINED ==========")
print(refine_text(text))
