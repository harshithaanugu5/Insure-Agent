from __future__ import annotations

import math
from collections import Counter


def generate_embedding(text: str) -> list[float]:
    tokens = [token.lower() for token in text.replace("\n", " ").split() if token.strip()]
    counts = Counter(tokens)
    total = sum(counts.values()) or 1
    vector = [count / total for count in counts.values()]
    if not vector:
        return [0.0]
    return [float(value) for value in vector]


def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    if not vec_a or not vec_b:
        return 0.0
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)
