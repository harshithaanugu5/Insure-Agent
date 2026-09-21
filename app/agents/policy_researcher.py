from __future__ import annotations

from app.rag.ingestion import load_policy_documents
from app.rag.hybrid_search import hybrid_search
from app.rag.vector_store import InMemoryVectorStore


def fetch_policy_evidence(query: str) -> list[str]:
    docs = load_policy_documents()
    store = InMemoryVectorStore(docs)
    return hybrid_search(store, query, limit=3)
