from __future__ import annotations

from app.rag.vector_store import InMemoryVectorStore


def hybrid_search(store: InMemoryVectorStore, query: str, limit: int = 3) -> list[str]:
    if not query:
        return []

    query_lower = query.lower()
    keyword_results = [doc for doc in store.documents if query_lower in doc.lower()]
    if not keyword_results:
        keyword_results = store.search(query, limit=limit)

    scored = []
    for doc in store.documents:
        score = 0
        for term in query_lower.split():
            if term in doc.lower():
                score += 2
        if any(term in doc.lower() for term in query_lower.split()):
            score += 1
        scored.append((score, doc))

    ranked = [doc for _, doc in sorted(scored, key=lambda item: item[0], reverse=True) if doc]
    results = list(dict.fromkeys(keyword_results + ranked))
    return results[:limit]
