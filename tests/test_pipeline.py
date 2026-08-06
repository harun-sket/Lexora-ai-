from pathlib import Path
from pprint import pprint

from languages.common.pipeline.executor import run_pipeline

INPUT = "tests/data/normalization_input.txt"

text = Path(INPUT).read_text(
    encoding="utf-8"
)

result = run_pipeline(text)

print()

print("=" * 60)
print("LEXORA END-TO-END PIPELINE")
print("=" * 60)

pprint(result)
