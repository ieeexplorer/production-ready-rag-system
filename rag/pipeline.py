from dataclasses import dataclass
from pathlib import Path


DATA_PATH = Path("data/sample_knowledge_base.txt")


@dataclass
class RAGResult:
    answer: str
    sources: list[str]


class SimpleRetriever:
    def __init__(self, data_path: Path):
        self.data_path = data_path
        self.documents = self._load_documents()

    def _load_documents(self) -> list[str]:
        if not self.data_path.exists():
            return ["Knowledge base file not found."]

        content = self.data_path.read_text(encoding="utf-8")
        return [chunk.strip() for chunk in content.split("\n\n") if chunk.strip()]

    def search(self, question: str) -> str:
        question_lower = question.lower()

        for document in self.documents:
            if any(word in document.lower() for word in question_lower.split()):
                return document

        return self.documents[0]


retriever = SimpleRetriever(DATA_PATH)


def answer_question(question: str) -> RAGResult:
    retrieved_context = retriever.search(question)

    answer = (
        "Based on the internal knowledge base, the system indicates:\n\n"
        f"{retrieved_context}"
    )

    return RAGResult(
        answer=answer,
        sources=[str(DATA_PATH)],
    )
