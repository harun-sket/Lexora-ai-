"""
Production Refinery Test

This simulates exactly what Lexora Brain does.
"""

from pathlib import Path

from languages.common.refinery.pipeline import refine_text

INPUT_FILE = "storage/uploads/tamil_test.txt"

text = Path(INPUT_FILE).read_text(
    encoding="utf-8",
    errors="replace",
)

result = refine_text(text)

print("\n========== INPUT ==========\n")
print(text)

print("\n========== OUTPUT ==========\n")
print(result)

Path("storage/output/refined_output.txt").parent.mkdir(
    parents=True,
    exist_ok=True,
)

Path("storage/output/refined_output.txt").write_text(
    result,
    encoding="utf-8",
)

print("\nSaved -> storage/output/refined_output.txt")
