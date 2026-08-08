from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from languages.tamil.pipeline import TamilPipeline

pipeline = TamilPipeline()

sample = ROOT / "tests" / "sample_input.txt"

print("=" * 80)
print("LEXORA REAL DATA TEST")
print("=" * 80)

for line in sample.read_text(encoding="utf-8").splitlines():
    line = line.strip()

    if not line:
        continue

    print("\n" + "=" * 80)
    print("INPUT:")
    print(line)

    result = pipeline.process(line)

    print("\nNORMALIZED:")
    print(result["normalized"])

    print("\nTOKENS:")
    print(result["tokens"])

    print("\nCORRECTED:")
    print(result["corrected_text"])

    if result["corrections"]:
        print("\nSPELL CHANGES:")
        for c in result["corrections"]:
            print(
                f"{c['original']}  ->  {c['corrected']} "
                f"(distance={c['distance']}, freq={c['frequency']})"
            )
    else:
        print("\nSPELL CHANGES:")
        print("None")

print("\n" + "=" * 80)
print("REAL TEST COMPLETE")
print("=" * 80)
