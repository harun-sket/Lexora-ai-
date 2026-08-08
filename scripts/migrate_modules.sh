#!/usr/bin/env bash

set -e

MODULES=(
normalize
tokenize
lexicon
resources
lemma
pipeline
)

for module in "${MODULES[@]}"
do
    FILE="languages/tamil/${module}.py"
    DIR="languages/tamil/${module}"

    if [ -f "$FILE" ]; then

        mkdir -p "$DIR"

        mv "$FILE" "$DIR/${module}.py"

        cat > "$DIR/__init__.py" <<EOPY
from .${module} import *
EOPY

        echo "✅ Migrated ${module}"
    else
        echo "⏭ Skipped ${module} (already migrated)"
    fi
done

echo
echo "🎉 Lexora module migration complete."
