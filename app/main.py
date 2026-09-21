from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.config import settings
from app.models.schemas import CustomerProfile, UnderwritingRequest

app = FastAPI(title=settings.app_name, version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "ok", "service": settings.app_name.lower().replace(" ", "-")}


@app.get("/api/policies")
def get_policies():
    return [
        {"id": "policy-auto-1", "name": "SafeDrive Plus", "type": "auto", "premium": 42.0, "coverage": 25000},
        {"id": "policy-home-1", "name": "HomeShield", "type": "home", "premium": 58.5, "coverage": 500000},
        {"id": "policy-life-1", "name": "Life Secure", "type": "life", "premium": 39.0, "coverage": 100000},
    ]


@app.post("/api/underwrite")
def submit_underwriting(request: UnderwritingRequest):
    from app.agents.orchestrator import orchestrate_underwriting

    result = orchestrate_underwriting(request.customer)
    return result


@app.get("/")
def root():
    return {"message": f"Welcome to {settings.app_name}. Use /health or /api/policies."}


@app.post("/api/quote")
def create_quote(customer: CustomerProfile):
    return {
        "customer_name": customer.customer_name,
        "policy_type": customer.policy_type,
        "annual_income": customer.annual_income,
        "estimated_premium": round(customer.requested_coverage / 10000 * 4.75, 2),
        "risk_note": "Underwriting review recommended for full assessment.",
    }


@app.post("/api/submit")
def submit_case(request: UnderwritingRequest):
    return {"status": "received", "customer": request.customer.model_dump()}
