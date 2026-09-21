from __future__ import annotations


class RiskModel:
    """Simple underwriting risk model used for demo purposes."""

    def predict(self, features: list[float] | list[int]) -> str:
        age, income, coverage, smoker_flag, medical_flag = features[:5]
        score = 20

        if age < 25:
            score += 25
        elif age > 60:
            score += 15

        if income < 40000:
            score += 15
        if coverage > 500000:
            score += 20
        if smoker_flag:
            score += 20
        if medical_flag:
            score += 15

        if score >= 70:
            return "High"
        if score >= 40:
            return "Medium"
        return "Low"
