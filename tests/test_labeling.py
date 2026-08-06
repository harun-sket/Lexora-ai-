"""
Lexora AI

Tamil Labeling Test
"""

from languages.tamil.lexora_labeling.label_engine import generate_labels


text = """
வணக்கம் நண்பர்களே.

எனக்கு ₹500 வேண்டும்.

தமிழ் AI மிகவும் சக்திவாய்ந்தது.
"""


labels = generate_labels(text)


print()

print("====================================")

print("LEXORA LABELING TEST")

print("====================================")

print()


for item in labels:

    print(item)

print()

print("TOTAL TOKENS :", len(labels))
