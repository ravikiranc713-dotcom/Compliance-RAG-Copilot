from app.services.retriever import (
    retriever
)

from app.services.bm25_store import (
    bm25_store
)


class HybridRetriever:

    def retrieve(
        self,
        question
    ):

        dense_results = (
            retriever.retrieve(
                question,
                top_k=10
            )
        )

        sparse_results = (
            bm25_store.search(
                question,
                top_k=10
            )
        )

        merged = []

        seen = set()

        for chunk in (
            dense_results +
            sparse_results
        ):

            if chunk not in seen:
                merged.append(chunk)
                seen.add(chunk)

        return merged


hybrid_retriever = HybridRetriever()