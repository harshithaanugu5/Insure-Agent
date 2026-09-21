from __future__ import annotations

from app.models.schemas import CustomerProfile


def analyze_documents(customer: CustomerProfile) -> dict:
    return {
        "customer_name": customer.customer_name,
        "age": customer.age,
        "annual_income": customer.annual_income,
        "requested_coverage": customer.requested_coverage,
        "smoking_status": customer.smoking_status,
        "medical_disclosure": customer.medical_disclosure,
        "policy_type": customer.policy_type,
        "status": "structured",
    }
