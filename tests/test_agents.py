from app.agents.orchestrator import orchestrate_underwriting
from app.models.schemas import CustomerProfile


def test_orchestrator_returns_recommendation():
    customer = CustomerProfile(
        customer_name="Jane Doe",
        age=36,
        annual_income=90000,
        requested_coverage=450000,
        smoking_status="non-smoker",
        medical_disclosure="No major issues.",
        policy_type="auto",
    )

    result = orchestrate_underwriting(customer)
    assert result["recommendation"] in {"APPROVE", "REVIEW", "DECLINE"}
    assert result["risk_score"] >= 0
    assert "key_factors" in result


def test_zero_income_requires_review():
    customer = CustomerProfile(
        customer_name="Zero Income Applicant",
        age=36,
        annual_income=0,
        requested_coverage=450000,
        smoking_status="non-smoker",
        medical_disclosure="No major issues.",
        policy_type="auto",
    )

    result = orchestrate_underwriting(customer)
    assert result["recommendation"] == "REVIEW"
    assert "Verified annual income" in result["missing_information"]


def test_coverage_above_ten_times_income_requires_review():
    customer = CustomerProfile(
        customer_name="Low Income Applicant",
        age=40,
        annual_income=780,
        requested_coverage=500000,
        smoking_status="non-smoker",
        medical_disclosure="No major issues.",
        policy_type="life",
    )

    result = orchestrate_underwriting(customer)
    assert result["recommendation"] == "REVIEW"
    assert "Coverage affordability verification" in result["missing_information"]


def test_underage_applicant_cannot_be_approved():
    customer = CustomerProfile.model_construct(
        customer_name="Underage Applicant",
        age=15,
        annual_income=85000,
        requested_coverage=100000,
        smoking_status="non-smoker",
        medical_disclosure="No major issues.",
        policy_type="life",
    )

    result = orchestrate_underwriting(customer)
    assert result["recommendation"] == "REVIEW"
    assert "Age must be between 18 and 90." in result["missing_information"]
