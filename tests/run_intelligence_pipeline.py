from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from languages.tamil.intelligence_pipeline import process

sample = ROOT / "tests" / "intelligence_input.txt"

print("=" * 100)
print("LEXORA LANGUAGE INTELLIGENCE PIPELINE")
print("=" * 100)

for line in sample.read_text(
    encoding="utf-8"
).splitlines():

    text = line.strip()

    if not text:
        continue

    result = process(text)

    print("\n" + "=" * 100)
    print("INPUT:")
    print(result["original"])

    print("\nLANGUAGE OBJECTS")

    for obj in result["objects"]:

        print(
            f"""
TEXT       : {obj.text}
KNOWN      : {obj.known}
FREQUENCY  : {obj.frequency}
ROOT       : {obj.root}
SUFFIXES   : {obj.suffixes}
POS        : {obj.pos}
ENTITY     : {obj.entity}
"""
        )

print("=" * 100)
print("PIPELINE COMPLETE")
print("=" * 100)
