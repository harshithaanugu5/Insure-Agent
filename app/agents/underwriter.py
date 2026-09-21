from __future__ import annotations


def decide_recommendation(risk_score: int) -> str:
    if risk_score >= 75:
        return "DECLINE"
    if risk_score >= 45:
        return "REVIEW"
    return "APPROVE"
