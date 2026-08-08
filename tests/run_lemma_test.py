from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from languages.tamil.lemma import lemmatize

sample = ROOT / "tests" / "lemma_input.txt"

print("=" * 80)
print("LEXORA LEMMATIZER TEST")
print("=" * 80)

for line in sample.read_text(
    encoding="utf-8"
).splitlines():

    word = line.strip()

    if not word:
        continue

    result = lemmatize(word)

    print("\n" + "=" * 80)
    print("WORD  :", result.word)
    print("LEMMA :", result.lemma)

print("\n" + "=" * 80)
print("LEMMATIZER TEST COMPLETE")
print("=" * 80)
