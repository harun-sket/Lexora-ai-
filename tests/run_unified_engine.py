from languages.tamil.unified_engine import process


def main():
    text = "இந்தியா சென்னை தமிழ் தம்பி"

    result = process(text)

    print("=" * 70)
    print("LEXORA TAMIL UNIFIED ENGINE v1.0")
    print("=" * 70)

    print("INPUT:")
    print(result["original"])

    print()
    print("TOKENS:")
    print(result["tokens"])

    print()
    print("ANALYSIS:")

    for item in result["analysis"]:
        print(
            f"{item['text']} | "
            f"known={item['known']} | "
            f"frequency={item['frequency']} | "
            f"pos={item['pos']} | "
            f"entity={item['entity']} | "
            f"corrected={item['corrected']} | "
            f"lemma={item['lemma']}"
        )

    print("=" * 70)


if __name__ == "__main__":
    main()
