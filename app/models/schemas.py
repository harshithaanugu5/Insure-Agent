from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field


class CustomerProfile(BaseModel):
    customer_name: str = Field(..., min_length=2)
    age: int = Field(..., ge=18, le=90)
    annual_income: float = Field(..., ge=0)
    requested_coverage: float = Field(..., ge=10000)
    smoking_status: Literal["smoker", "non-smoker"] = "non-smoker"
    medical_disclosure: str = ""
    policy_type: str = "auto"


class UnderwritingRequest(BaseModel):
    customer: CustomerProfile


class RecommendationResponse(BaseModel):
    recommendation: str
    risk_score: int
    risk_level: str
    key_factors: list[str]
    missing_information: list[str]
    policy_evidence: list[str]
    next_actions: list[str]
