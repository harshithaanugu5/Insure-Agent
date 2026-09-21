from __future__ import annotations


def evaluate_retrieval(results: list[str]) -> dict:
    return {
        "retrieved_count": len(results),
        "relevance_score": min(1.0, len(results) / 3),
        "status": "ok",
    }
