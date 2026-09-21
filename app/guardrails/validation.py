from __future__ import annotations


def validate_customer_profile(customer: object) -> list[str]:
    issues: list[str] = []

    age = getattr(customer, "age", None)
    if age is None:
        issues.append("Age is missing.")
    elif age < 18 or age > 90:
        issues.append("Age must be between 18 and 90.")

    income = getattr(customer, "annual_income", None)
    if income is None:
        issues.append("Annual income is missing.")
    elif income < 0:
        issues.append("Annual income cannot be negative.")

    coverage = getattr(customer, "requested_coverage", None)
    if coverage is None:
        issues.append("Requested coverage is missing.")
    elif coverage < 10000:
        issues.append("Requested coverage must be at least $10,000.")

    if getattr(customer, "customer_name", "").strip() == "":
        issues.append("Customer name is required.")

    return issues
