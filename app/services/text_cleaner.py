import re


class TextCleaner:

    def clean(self, text: str) -> str:

        # Remove multiple spaces
        text = re.sub(r"\s+", " ", text)

        # Remove repeated newlines
        text = re.sub(r"\n+", "\n", text)

        # Remove tabs
        text = text.replace("\t", " ")

        return text.strip()


text_cleaner = TextCleaner()