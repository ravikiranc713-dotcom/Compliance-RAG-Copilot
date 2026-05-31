import os
import pickle
import faiss
import numpy as np

from app.config import settings


class VectorStore:

    def __init__(self):

        self.index = None
        self.chunks = []

    def build_index(
        self,
        embeddings,
        chunks
    ):

        embeddings = np.array(
            embeddings
        ).astype("float32")

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(embeddings)

        self.chunks = chunks

    def save(self):

        faiss.write_index(
            self.index,
            os.path.join(
                settings.FAISS_INDEX_PATH,
                "index.faiss"
            )
        )

        with open(
            os.path.join(
                settings.FAISS_INDEX_PATH,
                "chunks.pkl"
            ),
            "wb"
        ) as f:

            pickle.dump(
                self.chunks,
                f
            )

    def load(self):

        self.index = faiss.read_index(
            os.path.join(
                settings.FAISS_INDEX_PATH,
                "index.faiss"
            )
        )

        with open(
            os.path.join(
                settings.FAISS_INDEX_PATH,
                "chunks.pkl"
            ),
            "rb"
        ) as f:

            self.chunks = pickle.load(f)


vector_store = VectorStore()