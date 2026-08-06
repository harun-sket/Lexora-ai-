from pathlib import Path
from pprint import pprint

from languages.common.labeling.labeler import label_text

text = Path("tests/data/label_input.txt").read_text(encoding="utf-8")

result = label_text(text)

pprint(result)
