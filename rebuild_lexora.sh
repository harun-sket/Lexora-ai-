#!/usr/bin/env bash
set -euo pipefail

echo "========================================"
echo " Rebuilding Lexora Foundation"
echo "========================================"

# Create directory structure
mkdir -p \
languages/tamil/normalize \
languages/tamil/tokenize \
languages/tamil/spell/data \
languages/tamil/morphology \
languages/tamil/pos \
languages/tamil/ner \
languages/tamil/transliterate \
languages/tamil/embeddings \
tests

# Create package markers
find languages -type d -exec touch {}/__init__.py \;

# Core files
touch languages/tamil/pipeline.py

touch languages/tamil/normalize/normalizer.py
touch languages/tamil/tokenize/tokenizer.py

touch languages/tamil/spell/symspell_engine.py
touch languages/tamil/spell/build_dictionary.py

touch languages/tamil/morphology/analyzer.py
touch languages/tamil/pos/tagger.py
touch languages/tamil/ner/recognizer.py
touch languages/tamil/transliterate/transliterator.py
touch languages/tamil/embeddings/embedder.py

# Tests
touch tests/test_normalizer.py
touch tests/test_tokenizer.py
touch tests/test_symspell.py
touch tests/test_pipeline.py

echo
echo "========================================"
echo " Lexora foundation rebuilt."
echo "========================================"
echo

find languages -maxdepth 3 -type f | sort

