from __future__ import annotations


def sample_dataset() -> list[dict]:
    return [
        {
            "customer_name": "Jane Doe",
            "age": 36,
            "annual_income": 90000,
            "requested_coverage": 450000,
            "smoking_status": "non-smoker",
            "medical_disclosure": "No major issues",
            "policy_type": "auto",
        },
        {
            "customer_name": "John Smith",
            "age": 61,
            "annual_income": 55000,
            "requested_coverage": 800000,
            "smoking_status": "smoker",
            "medical_disclosure": "Hypertension",
            "policy_type": "home",
        },
    ]
