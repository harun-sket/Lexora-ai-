from __future__ import annotations

import traceback
from datetime import datetime
from pathlib import Path

from languages.tamil.unified_engine import (
    ENGINE_NAME,
    ENGINE_VERSION,
    process,
)


TRACEBACK_DIR = Path(__file__).resolve().parent / "tracebacks"


def save_traceback() -> Path:
    TRACEBACK_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = (
        TRACEBACK_DIR
        / f"unified_contract_{timestamp}.txt"
    )

    with output_file.open("w", encoding="utf-8") as f:
        f.write("=" * 80)
        f.write("\nLEXORA UNIFIED CONTRACT TRACEBACK\n")
        f.write("=" * 80)
        f.write("\n\n")
        f.write(traceback.format_exc())
        f.write("\n")

    return output_file


def main() -> None:
    try:
        text = "இந்தியா சென்னை தமிழ்"

        result = process(text)

        print("=" * 70)
        print("LEXORA UNIFIED OUTPUT CONTRACT")
        print("=" * 70)

        assert isinstance(result, dict), (
            f"Expected dict, got {type(result).__name__}"
        )

        assert result.get("engine") == ENGINE_NAME, (
            f"engine mismatch: {result.get('engine')!r}"
        )

        assert result.get("version") == ENGINE_VERSION, (
            f"version mismatch: {result.get('version')!r}"
        )

        assert result.get("original") == text, (
            f"original mismatch: {result.get('original')!r}"
        )

        tokens = result.get("tokens")
        analysis = result.get("analysis")

        assert isinstance(tokens, list), (
            f"tokens should be list, got {type(tokens).__name__}"
        )

        assert isinstance(analysis, list), (
            f"analysis should be list, got {type(analysis).__name__}"
        )

        assert len(tokens) == len(analysis), (
            f"token/analysis length mismatch: "
            f"{len(tokens)} != {len(analysis)}"
        )

        required_fields = {
            "text",
            "normalized",
            "corrected",
            "lemma",
            "known",
            "frequency",
            "pos",
            "entity",
            "morphology",
        }

        for index, item in enumerate(analysis):
            assert isinstance(item, dict), (
                f"analysis[{index}] should be dict, "
                f"got {type(item).__name__}"
            )

            missing = required_fields - item.keys()

            assert not missing, (
                f"analysis[{index}] missing fields: "
                f"{sorted(missing)}"
            )

            assert isinstance(item["text"], str)
            assert isinstance(item["normalized"], str)
            assert isinstance(item["corrected"], str)
            assert isinstance(item["lemma"], str)
            assert isinstance(item["known"], bool)
            assert isinstance(item["frequency"], int)
            assert isinstance(item["pos"], str)
            assert isinstance(item["entity"], str)

        print("Engine       : GREEN 🟢")
        print("Version      : GREEN 🟢")
        print("Tokens       : GREEN 🟢")
        print("Analysis     : GREEN 🟢")
        print("Fields       : GREEN 🟢")
        print()
        print("CONTRACT     : GREEN 🟢")
        print("=" * 70)

    except Exception:
        output_file = save_traceback()

        print()
        print("❌ TEST FAILED")
        print()
        print(f"Traceback saved to:")
        print(output_file)
        print()
        print("Open it with:")
        print(f"cat {output_file}")

        raise


if __name__ == "__main__":
    main()
