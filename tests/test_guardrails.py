from app.guardrails.validation import validate_customer_profile
from app.models.schemas import CustomerProfile


def test_customer_validation_accepts_valid_profile():
    customer = CustomerProfile(
        customer_name="John Smith",
        age=42,
        annual_income=120000,
        requested_coverage=350000,
        smoking_status="non-smoker",
        medical_disclosure="No major conditions.",
        policy_type="home",
    )

    assert validate_customer_profile(customer) == []


def test_customer_validation_flags_bad_profile():
    customer = CustomerProfile.model_construct(
        customer_name="",
        age=10,
        annual_income=-50,
        requested_coverage=5000,
        smoking_status="non-smoker",
        medical_disclosure="",
        policy_type="home",
    )

    issues = validate_customer_profile(customer)
    assert any("Customer name" in issue for issue in issues)
    assert any("Age" in issue for issue in issues)
