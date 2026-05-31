import numpy as np

from app.config import settings
from app.services.embedding_service import (
    embedding_service
)
from app.services.vector_store import (
    vector_store
)


class Retriever:

    def retrieve(
        self,
        question: str,
        top_k: int = None
    ):

        if top_k is None:
            top_k = settings.TOP_K

        query_embedding = (
            embedding_service.embed_query(
                question
            )
        )

        query_embedding = np.array(
            [query_embedding]
        ).astype("float32")

        distances, indices = (
            vector_store.index.search(
                query_embedding,
                top_k
            )
        )

        retrieved_chunks = []

        for idx in indices[0]:

            if idx < len(
                vector_store.chunks
            ):
                retrieved_chunks.append(
                    vector_store.chunks[idx]
                )

        return retrieved_chunks


retriever = Retriever()