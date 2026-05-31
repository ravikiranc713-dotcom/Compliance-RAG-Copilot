from fastapi import APIRouter

from app.models.request_models import (
    QueryRequest
)

from app.models.response_models import (
    QueryResponse
)

from app.services.retriever import (
    retriever
)

from app.services.prompt_builder import (
    prompt_builder
)

from app.services.llm_service import (
    llm_service
)

from app.services.hybrid_retriever import (
    hybrid_retriever
)

from app.services.reranker import (
    reranker
)



router = APIRouter()


@router.post(
    "/query",
    response_model=QueryResponse
)
async def query_document(
    request: QueryRequest
):

    candidate_chunks = (
    hybrid_retriever.retrieve(
        request.question
    )
)

    chunks = reranker.rerank(
    request.question,
    candidate_chunks,
    top_k=5
)

    prompt = (
        prompt_builder.build_prompt(
            request.question,
            chunks
        )
    )

    answer = llm_service.generate(
        prompt
    )

    return QueryResponse(
        answer=answer,
        sources=chunks
    )