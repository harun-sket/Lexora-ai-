from languages.tamil.intelligence import process


def main():
    text = "இந்தியா சென்னை தமிழ்"

    result = process(text)

    print("=" * 70)
    print("LEXORA UNIFIED INTELLIGENCE ENGINE")
    print("=" * 70)

    print(f"Original: {result['original']}")
    print(f"Tokens: {result['tokens']}")
    print()

    for item in result["analysis"]:
        print(
            f"{item['text']} | "
            f"known={item['known']} | "
            f"frequency={item['frequency']} | "
            f"pos={item['pos']} | "
            f"entity={item['entity']}"
        )

    print("=" * 70)


if __name__ == "__main__":
    main()
