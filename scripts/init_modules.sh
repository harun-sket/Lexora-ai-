#!/usr/bin/env bash

set -e

mkdir -p languages/tamil/{normalize,tokenize,spell,lexicon,morphology,lemma,pos,ner,embeddings,resources,intelligence,pipeline,token}

for dir in \
normalize \
tokenize \
spell \
lexicon \
morphology \
lemma \
pos \
ner \
embeddings \
resources \
intelligence \
pipeline \
token
do
    touch "languages/tamil/$dir/__init__.py"
done

mkdir -p tests

echo "✅ Lexora module structure initialized."
