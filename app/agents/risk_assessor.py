from __future__ import annotations

from app.models.risk_model import RiskModel
from app.tools.calculator import calculate_risk_score, classify_risk


def assess_risk(customer: object) -> dict:
    risk_score = calculate_risk_score(customer)
    risk_label = classify_risk(risk_score)
    model = RiskModel()
    features = [
        getattr(customer, "age", 40),
        getattr(customer, "annual_income", 60000),
        getattr(customer, "requested_coverage", 250000),
        1 if getattr(customer, "smoking_status", "non-smoker") == "smoker" else 0,
        1 if getattr(customer, "medical_disclosure", "").strip() else 0,
    ]
    model_label = model.predict(features)
    return {
        "risk_score": risk_score,
        "risk_level": risk_label,
        "model_label": model_label,
    }
