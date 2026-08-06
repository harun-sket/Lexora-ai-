from pathlib import Path

from languages.common.normalization.indic_normalizer import normalize_text

text = Path(
    "tests/data/normalization_input.txt"
).read_text(encoding="utf-8")

print("========== ORIGINAL ==========")
print(text)

print("\n========== NORMALIZED ==========")
print(normalize_text(text, "ta"))
