class PromptBuilder:

    def build_prompt(
        self,
        question,
        chunks
    ):

        context = "\n\n".join(chunks)

        prompt = f"""
You are a helpful assistant.

Answer ONLY from the provided context.

If the answer is not available in the context,
say:

"I could not find the answer in the document."

Context:
{context}

Question:
{question}

Answer:
"""

        return prompt


prompt_builder = PromptBuilder()