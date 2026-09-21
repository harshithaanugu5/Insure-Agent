from __future__ import annotations

from typing import Iterable


class InMemoryVectorStore:
    """A lightweight in-memory vector store used for local policy retrieval."""

    def __init__(self, documents: Iterable[str] | None = None):
        self.documents = list(documents or [])

    def add(self, docs: Iterable[str]) -> None:
        self.documents.extend(list(docs))

    def search(self, query: str, limit: int = 3) -> list[str]:
        query_lower = query.lower()
        matches = [doc for doc in self.documents if query_lower in doc.lower()]
        return matches[:limit]
