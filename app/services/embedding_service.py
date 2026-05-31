from sentence_transformers import (
    SentenceTransformer
)

from app.config import settings


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(
            settings.EMBEDDING_MODEL
        )

    def embed_documents(
        self,
        chunks
    ):

        return self.model.encode(
            chunks,
            show_progress_bar=True
        )

    def embed_query(
        self,
        query
    ):

        return self.model.encode(
            [query]
        )[0]


embedding_service = EmbeddingService()