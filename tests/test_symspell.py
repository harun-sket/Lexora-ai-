from pathlib import Path
import sys
import traceback

# -------------------------------------------------
# Add project root to Python path
# -------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

print("=" * 60)
print("PROJECT ROOT")
print(ROOT)
print("=" * 60)

print("\nPython Path:\n")
for p in sys.path:
    print(p)

print("\nTrying import...\n")

try:
    from languages.tamil.spell.symspell_engine import (
        correct_word,
        suggest,
    )

    print("✅ IMPORT SUCCESS")

    words = [
        "வணக்கம",
        "தமிழ",
        "மொழி",
        "அரசங",
        "கல்வி",
    ]

    print("\nTesting corrections:\n")

    for word in words:
        print("-" * 50)
        print("Input :", word)

        result = correct_word(word)

        print(result)

        print("\nSuggestions:")

        for s in suggest(word)[:5]:
            print(" ", s)

except Exception:
    print("\n❌ IMPORT FAILED\n")
    traceback.print_exc()

    trace_file = ROOT / "symspell_traceback.txt"

    with open(trace_file, "w", encoding="utf-8") as f:
        traceback.print_exc(file=f)

    print(f"\nTraceback saved to:\n{trace_file}")

