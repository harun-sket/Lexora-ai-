from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from languages.tamil.token import create_token

words = [
    "தமிழ்",
    "தம்ழி",
    "AI",
    "123",
    "!!!",
    "இந்தியா",
    "கணினி",
    "Hello",
    "தமிழ்123",
]

print("=" * 100)
print("LEXORA LANGUAGE OBJECT TEST")
print("=" * 100)

for word in words:

    token = create_token(word)

    print(f"""
TEXT           : {token.text}

TOKEN TYPE     : {token.token_type}

CORRECTED      : {token.corrected}
SPELL CHANGED  : {token.changed}
EDIT DISTANCE  : {token.edit_distance}

KNOWN          : {token.known}
FREQUENCY      : {token.frequency}

ROOT           : {token.root}
SUFFIXES       : {token.suffixes}

POS            : {token.pos}
ENTITY         : {token.entity}
""")

print("=" * 100)
print("LANGUAGE OBJECT TEST COMPLETE")
print("=" * 100)
