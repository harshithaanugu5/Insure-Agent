from __future__ import annotations

MAX_COVERAGE_TO_INCOME_MULTIPLE = 10


def exceeds_coverage_income_limit(customer: object) -> bool:
    income = getattr(customer, "annual_income", 0)
    coverage = getattr(customer, "requested_coverage", 0)
    return income <= 0 or coverage > income * MAX_COVERAGE_TO_INCOME_MULTIPLE


def calculate_risk_score(customer: object) -> int:
    age = getattr(customer, "age", 40)
    income = getattr(customer, "annual_income", 50000)
    coverage = getattr(customer, "requested_coverage", 200000)
    smoking = getattr(customer, "smoking_status", "non-smoker")
    medical = getattr(customer, "medical_disclosure", "")

    score = 18

    if age < 25:
        score += 18
    elif age > 60:
        score += 16
    elif age > 45:
        score += 9

    if income < 40000:
        score += 12
    elif income > 150000:
        score -= 5

    if coverage > 750000:
        score += 18
    elif coverage > 300000:
        score += 10

    if exceeds_coverage_income_limit(customer):
        score += 20

    if smoking == "smoker":
        score += 20

    if medical and "hypertension" in medical.lower():
        score += 12
    if medical and "diabetes" in medical.lower():
        score += 14

    score = max(0, min(100, score))
    return score


def classify_risk(score: int) -> str:
    if score >= 75:
        return "High"
    if score >= 45:
        return "Medium"
    return "Low"
