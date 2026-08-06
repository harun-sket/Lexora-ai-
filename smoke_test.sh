#!/usr/bin/env bash
set -e

echo "========================================"
echo "       LEXORA FOUNDATION TEST"
echo "========================================"

echo
echo "[1/5] Checking project structure..."
find languages -maxdepth 3 -type f | sort

echo
echo "[2/5] Importing pipeline..."
python - << 'PY'
from languages.tamil.pipeline import TamilPipeline
print("✅ TamilPipeline imported successfully")
PY

echo
echo "[3/5] Running pipeline..."
python - << 'PY'
from languages.tamil.pipeline import TamilPipeline

pipeline = TamilPipeline()

samples = [
    "வணக்கம்",
    "நான் தமிழ் பேசுகிறேன்",
    "தம்ழி",
    "வனக்கம்",
]

for text in samples:
    print("=" * 50)
    print("INPUT :", text)
    result = pipeline.process(text)
    print(result)
PY

echo
echo "[4/5] Running unit tests..."
python -m pytest tests -v

echo
echo "[5/5] Foundation verified."

echo
echo "========================================"
echo "✅ LEXORA FOUNDATION IS STABLE"
echo "========================================"
