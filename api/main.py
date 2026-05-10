from fastapi import FastAPI
from pydantic import BaseModel, Field

from guardrails.input_checks import check_question
from observability.logger import get_logger
from rag.pipeline import answer_question

logger = get_logger(__name__)

app = FastAPI(
    title="Production-Ready RAG System",
    description="API backend for a production-style Retrieval-Augmented Generation system.",
    version="0.1.0",
)


class AskRequest(BaseModel):
    question: str = Field(..., min_length=3, description="User question to answer from the knowledge base")


class AskResponse(BaseModel):
    answer: str
    sources: list[str]
    blocked: bool = False
    reason: str | None = None


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "production-ready-rag-system"}


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest) -> AskResponse:
    logger.info("Received question", extra={"question_length": len(request.question)})

    guardrail_result = check_question(request.question)
    if not guardrail_result.allowed:
        logger.warning("Question blocked by guardrails", extra={"reason": guardrail_result.reason})
        return AskResponse(
            answer="I cannot answer this request because it failed the safety checks.",
            sources=[],
            blocked=True,
            reason=guardrail_result.reason,
        )

    result = answer_question(request.question)
    return AskResponse(answer=result.answer, sources=result.sources, blocked=False)
