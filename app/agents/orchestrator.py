from __future__ import annotations

from app.guardrails.validation import validate_customer_profile
from app.rag.ingestion import load_policy_documents
from app.tools.calculator import (
    calculate_risk_score,
    classify_risk,
    exceeds_coverage_income_limit,
)


def orchestrate_underwriting(customer: object) -> dict:
    issues = validate_customer_profile(customer)
    risk_score = calculate_risk_score(customer)
    risk_level = classify_risk(risk_score)
    evidence = load_policy_documents()

    key_factors: list[str] = []
    if getattr(customer, "smoking_status", "non-smoker") == "smoker":
        key_factors.append("Smoking status increases underwriting risk.")
    if getattr(customer, "requested_coverage", 0) > 300000:
        key_factors.append("Requested coverage exceeds the standard threshold.")
    if getattr(customer, "medical_disclosure", "").strip():
        key_factors.append("Medical information requires additional review.")
    if getattr(customer, "annual_income", 0) <= 0:
        key_factors.append("Annual income must be verified before underwriting approval.")
    if exceeds_coverage_income_limit(customer):
        key_factors.append("Requested coverage exceeds 10 times annual income.")
    if not key_factors:
        key_factors.append("Customer profile is within the standard underwriting range.")

    if issues or exceeds_coverage_income_limit(customer):
        recommendation = "REVIEW"
    elif risk_score >= 75:
        recommendation = "DECLINE"
    elif risk_score >= 45:
        recommendation = "REVIEW"
    else:
        recommendation = "APPROVE"

    missing = []
    if not getattr(customer, "medical_disclosure", "").strip():
        missing.append("Medical disclosure")
    if not getattr(customer, "policy_type", "").strip():
        missing.append("Policy type")
    if getattr(customer, "annual_income", 0) <= 0:
        missing.append("Verified annual income")
    if exceeds_coverage_income_limit(customer):
        missing.append("Coverage affordability verification")

    next_actions = [
        "Review policy evidence before making a final decision.",
        "Confirm any missing medical or eligibility details.",
    ]

    return {
        "recommendation": recommendation,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "key_factors": key_factors,
        "missing_information": missing + issues,
        "policy_evidence": evidence[:3],
        "next_actions": next_actions,
    }
