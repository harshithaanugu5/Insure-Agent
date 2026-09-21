from __future__ import annotations


def rerank_results(results: list[str], query: str) -> list[str]:
    query_lower = query.lower()

    def score(doc: str) -> int:
        return sum(2 for term in query_lower.split() if term in doc.lower())

    return [doc for doc, _ in sorted(((doc, score(doc)) for doc in results), key=lambda item: item[1], reverse=True)]
