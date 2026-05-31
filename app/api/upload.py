import os
import shutil

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.config import settings

from app.services.pdf_processor import pdf_processor
from app.services.chunker import chunker
from app.services.embedding_service import (
    embedding_service
)
from app.services.vector_store import (
    vector_store
)
from app.services.bm25_store import (
    bm25_store
)
router = APIRouter()


@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    pdf_path = os.path.join(
        settings.PDF_STORAGE,
        file.filename
    )

    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    text = pdf_processor.extract_text(
        pdf_path
    )

    chunks = chunker.split_text(text)

    embeddings = (
        embedding_service.embed_documents(
            chunks
        )
    )

    vector_store.build_index(
        embeddings,
        chunks
    )



    bm25_store.build(chunks)

    bm25_store.save()

    vector_store.save()

    return {
        "filename": file.filename,
        "chunks": len(chunks),
        "status": "indexed"
    }