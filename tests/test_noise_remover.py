from pathlib import Path

from languages.common.refinery.noise_remover import remove_noise

INPUT_FILE = "tests/data/noise_input.txt"

text = Path(INPUT_FILE).read_text(encoding="utf-8")

print("========== ORIGINAL ==========")
print(text)

print("\n========== CLEANED ==========")
print(remove_noise(text))
