import pickle
from rank_bm25 import BM25Okapi


class BM25Store:

    def __init__(self):
        self.bm25 = None
        self.chunks = []

    def build(self, chunks):

        tokenized = [
            chunk.lower().split()
            for chunk in chunks
        ]

        self.bm25 = BM25Okapi(tokenized)

        self.chunks = chunks

    def search(
        self,
        query,
        top_k=10
    ):

        tokenized_query = (
            query.lower().split()
        )

        scores = self.bm25.get_scores(
            tokenized_query
        )

        ranked = sorted(
            zip(self.chunks, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return [
            chunk
            for chunk, _
            in ranked[:top_k]
        ]

    def save(self):

        with open(
            "data/faiss_index/bm25.pkl",
            "wb"
        ) as f:

            pickle.dump(
                self,
                f
            )

    @staticmethod
    def load():

        with open(
            "data/faiss_index/bm25.pkl",
            "rb"
        ) as f:

            return pickle.load(f)


bm25_store = BM25Store()