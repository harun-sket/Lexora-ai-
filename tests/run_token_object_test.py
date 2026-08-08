from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from languages.tamil.token import create_token

sample = ROOT / "tests" / "token_input.txt"

print("=" * 90)
print("LEXORA TOKEN OBJECT TEST")
print("=" * 90)

for line in sample.read_text(
    encoding="utf-8"
).splitlines():

    word = line.strip()

    if not word:
        continue

    token = create_token(word)

    print("\n" + "=" * 90)
    print("WORD :", word)

    print("KNOWN      :", token.known)
    print("FREQUENCY  :", token.frequency)
    print("ROOT       :", token.root)
    print("SUFFIXES   :", token.suffixes)
    print("POS        :", token.pos)
    print("ENTITY     :", token.entity)

print("\n" + "=" * 90)
print("TOKEN OBJECT TEST COMPLETE")
print("=" * 90)
