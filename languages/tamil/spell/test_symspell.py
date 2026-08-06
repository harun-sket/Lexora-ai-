from pathlib import Path
import traceback

from symspell_engine import (
    get_symspell,
    correct_word,
    suggest,
)

print("=" * 70)
print("LEXORA TAMIL SYMSPELL TEST")
print("=" * 70)

try:
    engine = get_symspell()

    print("\n✅ Dictionary Loaded Successfully")
    print(f"Dictionary : {engine.dictionary_path}")

    words = [
        "வணக்கம",
        "தமிழ",
        "மொழி",
        "கல்வி",
        "மனிதன",
        "அரசங",
        "நண்பர்கலே",
        "புத்தகம",
        "கணினி",
        "மரம",
    ]

    print("\n" + "=" * 70)
    print("TEST RESULTS")
    print("=" * 70)

    for word in words:
        result = correct_word(word)

        print(f"\nInput      : {word}")

        if result is None:
            print("No suggestion")
            continue

        print(f"Corrected  : {result['corrected']}")
        print(f"Distance   : {result['distance']}")
        print(f"Frequency  : {result['frequency']}")
        print(f"Changed    : {result['changed']}")

        print("Top Suggestions:")

        suggestions = suggest(word)[:5]

        if not suggestions:
            print("  (none)")
            continue

        for i, s in enumerate(suggestions, start=1):
            print(
                f"  {i}. "
                f"{s['term']} "
                f"(distance={s['distance']}, "
                f"freq={s['frequency']})"
            )

except Exception:
    print("\n❌ ERROR\n")
    traceback.print_exc()

    trace_file = Path(__file__).parent / "symspell_traceback.txt"

    with open(trace_file, "w", encoding="utf-8") as f:
        traceback.print_exc(file=f)

    print(f"\nTraceback saved to:\n{trace_file}")

