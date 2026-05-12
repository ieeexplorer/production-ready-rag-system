import chromadb
from chromadb.config import Settings
import os


class VectorStore:
    def __init__(self, persist_dir="./data/chroma"):
        os.makedirs(persist_dir, exist_ok=True)

        self.client = chromadb.PersistentClient(path=persist_dir)

        self.collection = self.client.get_or_create_collection(
            name="enterprise_knowledge_base",
            metadata={"hnsw:space": "cosine"}
        )

    def add_documents(self, documents, embeddings, ids):
        self.collection.add(
            documents=documents,
            embeddings=embeddings,
            ids=ids
        )

    def hybrid_search(self, query_embedding, query_text, n_results=5):
        semantic_results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        return semantic_results
