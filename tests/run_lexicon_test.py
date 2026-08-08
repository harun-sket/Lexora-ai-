from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from languages.tamil.lexicon import (
    lookup,
    vocabulary_size,
)

sample = ROOT / "tests" / "lexicon_input.txt"

print("=" * 80)
print("LEXORA LEXICON TEST")
print("=" * 80)

print(f"\nVocabulary Size : {vocabulary_size():,}")

for line in sample.read_text(
    encoding="utf-8"
).splitlines():

    word = line.strip()

    if not word:
        continue

    result = lookup(word)

    print("\n" + "=" * 80)
    print("WORD :", word)

    if result is None:
        print("STATUS : UNKNOWN")
    else:
        print("STATUS : KNOWN")
        print("FREQUENCY :", result.frequency)

print("\n" + "=" * 80)
print("LEXICON TEST COMPLETE")
print("=" * 80)
