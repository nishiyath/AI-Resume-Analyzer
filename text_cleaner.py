import re


def clean_text(text):
    # Convert all text to lowercase
    text = text.lower()

    # Keep important technical symbols such as +, #, and .
    text = re.sub(r"[^a-zA-Z0-9+#.\-\s]", " ", text)

    # Remove extra spaces and line breaks
    text = re.sub(r"\s+", " ", text)

    # Remove spaces from the beginning and end
    text = text.strip()

    return text