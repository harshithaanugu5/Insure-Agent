from __future__ import annotations

from fastapi import APIRouter

from app.agents.orchestrator import orchestrate_underwriting
from app.models.schemas import CustomerProfile, RecommendationResponse, UnderwritingRequest

router = APIRouter(prefix="/api")


@router.get("/policies")
def list_policies():
    return [
        {"id": "policy-auto-1", "name": "SafeDrive Plus", "type": "auto", "premium": 42.0, "coverage": 25000},
        {"id": "policy-home-1", "name": "HomeShield", "type": "home", "premium": 58.5, "coverage": 500000},
        {"id": "policy-life-1", "name": "Life Secure", "type": "life", "premium": 39.0, "coverage": 100000},
    ]


@router.post("/underwrite", response_model=RecommendationResponse)
def submit_underwriting(request: UnderwritingRequest):
    result = orchestrate_underwriting(request.customer)
    return RecommendationResponse(**result)
