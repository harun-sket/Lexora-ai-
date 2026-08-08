from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from languages.tamil.morphology import analyze

sample = ROOT / "tests" / "morphology_input.txt"

print("=" * 80)
print("LEXORA MORPHOLOGY TEST")
print("=" * 80)

for line in sample.read_text(encoding="utf-8").splitlines():

    word = line.strip()

    if not word:
        continue

    result = analyze(word)

    print("\n" + "=" * 80)
    print("WORD      :", result.word)
    print("ROOT      :", result.root)
    print("SUFFIXES  :", result.suffixes)

print("\n" + "=" * 80)
print("MORPHOLOGY TEST COMPLETE")
print("=" * 80)
