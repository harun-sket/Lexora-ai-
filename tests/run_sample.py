from pathlib import Path
import sys

# Project root
ROOT = Path(__file__).resolve().parents[1]

# Add project root to Python path
sys.path.insert(0, str(ROOT))

print("Project root:", ROOT)

from languages.tamil.pipeline import TamilPipeline

pipeline = TamilPipeline()

sample = ROOT / "tests" / "sample_input.txt"

print("=" * 60)
print("LEXORA REAL PIPELINE TEST")
print("=" * 60)

for line in sample.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line:
        continue

    print(f"\nINPUT : {line}")
    print(pipeline.process(line))
