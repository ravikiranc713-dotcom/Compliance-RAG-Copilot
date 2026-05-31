'''
from fastapi import FastAPI

app = FastAPI(
    title="PDF RAG Chatbot",
    version="1.0"
)


@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "model": "mistral"
    }
'''

from fastapi import FastAPI

from app.api.upload import (
    router as upload_router
)

from app.api.query import (
    router as query_router
)

from app.services.vector_store import (
    vector_store
)

app = FastAPI(
    title="Compliance Document RAG Chatbot"
)


@app.on_event("startup")
def startup():

    try:
        vector_store.load()
        print("FAISS loaded")
    except:
        print("No index found")


app.include_router(upload_router)
app.include_router(query_router)


@app.get("/")
def health():

    return {
        "status": "healthy"
    }