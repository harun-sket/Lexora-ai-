from pathlib import Path

from languages.common.refinery.whitespace_cleaner import clean_whitespace

INPUT_FILE = "tests/test_whitespace_input.txt"

text = Path(INPUT_FILE).read_text(encoding="utf-8")

result = clean_whitespace(text)

print("\n========== ORIGINAL ==========\n")
print(text)

print("\n========== CLEANED ==========\n")
print(result)
