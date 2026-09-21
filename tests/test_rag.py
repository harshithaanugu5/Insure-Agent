from app.rag.hybrid_search import hybrid_search
from app.rag.vector_store import InMemoryVectorStore
from app.models.risk_model import RiskModel


def test_hybrid_search_returns_matches():
    store = InMemoryVectorStore([
        "Applicants under age 25 require additional verification.",
        "Coverage above $750,000 requires enhanced review.",
        "Smoking status must be disclosed.",
    ])

    results = hybrid_search(store, "age 25 coverage review")
    assert len(results) >= 1
    assert any("age" in item.lower() or "coverage" in item.lower() for item in results)


def test_risk_model_predicts_bucket():
    model = RiskModel()
    features = [42, 90000, 450000, 0, 0]
    prediction = model.predict(features)
    assert prediction in {"Low", "Medium", "High"}
