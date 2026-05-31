from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    MODEL_NAME = os.getenv("MODEL_NAME", "mistral")

    OLLAMA_BASE_URL = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434"
    )

    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "BAAI/bge-small-en-v1.5"
    )

    FAISS_INDEX_PATH = os.getenv(
        "FAISS_INDEX_PATH",
        "data/faiss_index"
    )

    PDF_STORAGE = os.getenv(
        "PDF_STORAGE",
        "data/pdfs"
    )

    TOP_K = int(os.getenv("TOP_K", 5))


settings = Settings()