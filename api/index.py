from pathlib import Path
import sys

project_root = Path(__file__).resolve().parents[1]
if str(project_root) not in sys.path:
	sys.path.insert(0, str(project_root))

from fastapi import FastAPI

app = FastAPI(title="Insure Agent", version="0.1.0")


@app.get("/health")
def health_check():
	return {"status": "ok", "service": "insure-agent"}


@app.get("/api/policies")
def list_policies():
	return [
		{"id": "policy-auto-1", "name": "SafeDrive Plus", "type": "auto", "premium": 42.0, "coverage": 25000},
		{"id": "policy-home-1", "name": "HomeShield", "type": "home", "premium": 58.5, "coverage": 500000},
		{"id": "policy-life-1", "name": "Life Secure", "type": "life", "premium": 39.0, "coverage": 100000},
	]


@app.post("/api/underwrite")
def submit_underwriting(request: dict):
	from app.agents.orchestrator import orchestrate_underwriting
	from app.models.schemas import UnderwritingRequest

	validated_request = UnderwritingRequest.model_validate(request)
	return orchestrate_underwriting(validated_request.customer)

__all__ = ["app"]