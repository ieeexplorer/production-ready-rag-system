from rag.vector_store import VectorStore
from observability.logger import get_logger


logger = get_logger()


class EnterpriseRAGPipeline:
    def __init__(self, embedding_model=None):
        self.vector_store = VectorStore()
        self.embedding_model = embedding_model

    def rewrite_query(self, query: str) -> str:
        rewritten_query = query.strip()
        logger.info(f"Query rewritten: {rewritten_query}")
        return rewritten_query

    def compress_context(self, documents):
        compressed = documents[:3]
        logger.info("Context compression completed")
        return compressed

    def retrieve(self, query_embedding, query_text):
        results = self.vector_store.hybrid_search(
            query_embedding=query_embedding,
            query_text=query_text,
            n_results=5
        )

        logger.info("Hybrid retrieval completed")
        return results

    def generate_answer(self, query, retrieved_docs):
        context = "\n".join(retrieved_docs)

        answer = (
            f"Enterprise RAG response generated for query: {query}\n\n"
            f"Context used:\n{context}"
        )

        logger.info("Answer generation completed")

        return {
            "answer": answer,
            "sources": retrieved_docs,
            "blocked": False
        }

    def run(self, query, query_embedding):
        rewritten_query = self.rewrite_query(query)

        retrieval_results = self.retrieve(
            query_embedding=query_embedding,
            query_text=rewritten_query
        )

        retrieved_docs = retrieval_results.get("documents", [[]])[0]

        compressed_docs = self.compress_context(retrieved_docs)

        return self.generate_answer(query, compressed_docs)
