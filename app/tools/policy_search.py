from __future__ import annotations


def search_policy_documents(query: str, documents: list[str]) -> list[str]:
    query_lower = query.lower()
    matches = [doc for doc in documents if query_lower in doc.lower()]
    return matches[:5]
