from pathlib import Path

from languages.common.pipeline.document import Document

from languages.common.export.json_builder import to_json

from languages.common.quality.quality_analyzer import analyze_quality

from languages.common.confidence.confidence_scorer import score

text = Path(
    "tests/data/normalization_input.txt"
).read_text(encoding="utf-8")

doc = Document(raw_text=text)

doc.normalized_text = text

doc.quality = analyze_quality(text)

doc.confidence = score(doc.quality)

print(to_json(doc))
