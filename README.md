# Insure-Agent

Insure-Agent is a multi-agent insurance underwriting and risk assessment platform built around a RAG workflow, FastAPI backend, and user-facing dashboard. It is designed to support preliminary underwriting decisions by combining structured customer data, policy evidence, risk scoring, and agent-based reasoning.

## Project overview

This project demonstrates how an agentic AI system can assist with insurance underwriting by:
- extracting and structuring customer information,
- retrieving policy evidence,
- evaluating risk factors,
- checking missing information,
- generating a preliminary underwriting recommendation.

## Architecture

- Backend: FastAPI
- Frontend: Streamlit
- Agent orchestration: LangGraph
- Retrieval: ChromaDB + sentence embeddings
- Risk scoring: scikit-learn and business rules
- Testing: pytest
- Containerization: Docker

## Key features

- Document-aware underwriting workflow
- Hybrid policy retrieval
- Risk score and recommendation output
- Missing information detection
- Guardrails and validation
- API and frontend UI for demo usage

## Project structure

```text
insure-agent/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── agents/
│   ├── rag/
│   ├── models/
│   ├── tools/
│   ├── guardrails/
│   ├── evaluation/
│   └── api/
├── frontend/
│   └── streamlit_app.py
├── data/
│   ├── policies/
│   └── sample_customers/
├── tests/
├── scripts/
├── .env.example
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Quick start

### 1) Create a virtual environment

```powershell
cd "C:\Users\Admin\OneDrive\Desktop\insure-agent"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Install dependencies

```powershell
pip install -r requirements.txt
```

### 3) Configure environment variables

```powershell
copy .env.example .env
```

### 4) Run the backend

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5) Run the frontend

```powershell
streamlit run frontend/streamlit_app.py
```

### 6) Run tests

```powershell
pytest
```

## Example API endpoints

- GET /health
- GET /api/policies
- POST /api/underwrite

## Notes

This repository is structured as an MVP for the full insurance underwriting platform described in the project brief, and it is intended to be extended with richer retrieval, model evaluation, and multi-agent workflows.
