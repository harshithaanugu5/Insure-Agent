# Insure-Agent: Multi-Agent Insurance Underwriting & Risk Assessment Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)

## 📌 Project Overview

**Insure-Agent** is an Agentic RAG platform designed to assist with **insurance underwriting and risk assessment**. The system uses a multi-agent architecture to analyze customer information, retrieve relevant insurance policy provisions, evaluate risk factors, identify missing information, and generate a preliminary underwriting recommendation supported by policy evidence.

Unlike a traditional document chatbot, Insure-Agent combines **Retrieval-Augmented Generation (RAG), multi-agent orchestration, machine learning-based risk assessment, deterministic business rules, and evidence-based decision support** to automate and streamline preliminary underwriting workflows.

The platform is designed to demonstrate how modern **Agentic AI and Machine Learning Engineering** practices can be applied to enterprise insurance use cases.

> **Important:** Insure-Agent provides a preliminary decision-support recommendation and is not a substitute for a licensed insurance underwriter or a final insurance decision.

---

## 🚀 Key Features

### 🤖 Multi-Agent Orchestration

Uses **LangGraph** to coordinate specialized agents through a stateful workflow:

* **Document Analyzer Agent** — extracts and structures relevant information from customer documents.
* **Policy Research Agent** — retrieves relevant insurance policy clauses, eligibility criteria, exclusions, and requirements.
* **Risk Assessment Agent** — evaluates customer risk factors using a combination of ML predictions and business rules.
* **Underwriting Decision Agent** — combines customer information, risk assessment, policy evidence, and business rules to generate a preliminary recommendation.

### 🔎 Intelligent Hybrid Retrieval

Implements a hybrid retrieval pipeline combining:

* Semantic vector search
* Keyword search
* Metadata filtering
* Relevance ranking
* Policy-section retrieval

The system is designed to retrieve relevant clauses from long-form insurance policy documents, including eligibility requirements, exclusions, coverage limits, and underwriting conditions.

### 📄 Document Intelligence

Processes insurance policy and customer documents using:

* PDF extraction
* Text preprocessing
* Structure-aware chunking
* Metadata extraction
* Embedding generation
* Vector indexing

### 📊 Explainable Risk Assessment

Generates a preliminary risk score using customer information and relevant underwriting factors.

The system provides:

* Risk score
* Risk classification
* Key decision factors
* Supporting policy evidence
* Source citations
* Missing information
* Recommended next actions

### 🛡️ AI Guardrails

Includes validation and safety controls for:

* Unsupported recommendations
* Missing information
* Hallucination detection
* Prompt injection attempts
* PII handling
* Policy citation requirements
* Out-of-scope requests
* Deterministic business-rule validation

### 👤 Human-in-the-Loop Review

Underwriters can review:

* Customer information
* Retrieved policy evidence
* Risk factors
* Model output
* Preliminary recommendation

before making a final business decision.

### 📈 AI/ML Evaluation & Observability

Tracks and evaluates:

* Retrieval relevance
* Citation accuracy
* Answer relevance
* Faithfulness
* Hallucination rate
* Agent task success
* Tool-call success
* Response latency
* Model performance

---

## 🏗️ System Architecture

```text
                         ┌──────────────────┐
                         │      User        │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │  Streamlit UI    │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │  FastAPI Backend │
                         └────────┬─────────┘
                                  │
                                  ▼
                    ┌──────────────────────────┐
                    │   LangGraph Orchestrator │
                    └────────────┬─────────────┘
                                 │
             ┌───────────────────┼───────────────────┐
             │                   │                   │
             ▼                   ▼                   ▼
    ┌────────────────┐  ┌────────────────┐  ┌────────────────┐
    │ Document       │  │ Policy Research│  │ Risk Assessment│
    │ Analyzer Agent │  │ Agent          │  │ Agent          │
    └───────┬────────┘  └───────┬────────┘  └───────┬────────┘
            │                   │                   │
            ▼                   ▼                   ▼
     Customer Data        Policy Evidence      Risk Score
            │                   │                   │
            └───────────────────┼───────────────────┘
                                ▼
                     ┌─────────────────────┐
                     │ Underwriting        │
                     │ Decision Agent      │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Preliminary         │
                     │ Recommendation      │
                     └──────────┬──────────┘
                                │
                ┌───────────────┼────────────────┐
                ▼               ▼                ▼
           Decision        Risk Factors      Citations
           APPROVE          Risk Score        Evidence
           REVIEW
           DECLINE
```

---

## 🔄 How It Works

### Step 1 — Customer Input

The user provides customer information and/or uploads supporting documents.

Example:

```text
Age: 42
Annual Income: $85,000
Coverage Requested: $500,000
Smoking Status: Non-Smoker
Medical Disclosure: Hypertension
```

### Step 2 — Document Analysis

The Document Analyzer Agent extracts relevant information and converts unstructured documents into structured customer attributes.

### Step 3 — Policy Retrieval

The Policy Research Agent searches the insurance policy knowledge base using hybrid retrieval.

It identifies:

* Eligibility requirements
* Coverage limits
* Exclusions
* Medical requirements
* Documentation requirements
* Underwriting conditions

### Step 4 — Risk Assessment

The Risk Assessment Agent evaluates customer attributes using:

* Machine learning predictions
* Statistical/risk factors
* Deterministic business rules
* Policy constraints

Example:

```text
Risk Score: 68 / 100
Risk Level: Medium
```

### Step 5 — Missing Information Detection

If required information is missing, the system identifies the missing fields and can trigger another retrieval or request for additional information.

### Step 6 — Underwriting Recommendation

The Underwriting Decision Agent combines:

```text
Customer Information
        +
Risk Assessment
        +
Policy Evidence
        +
Business Rules
        ↓
Preliminary Recommendation
```

Example:

```text
Recommendation: REVIEW

Risk Score: 68 / 100

Key Factors:
- Medical disclosure requires additional documentation.
- Requested coverage exceeds the standard threshold.
- Policy requires additional medical underwriting.

Required Action:
Request supporting medical documentation.

Policy Evidence:
Policy Section 4.2
Policy Section 7.1
```

---

## 🔎 RAG Pipeline

The retrieval pipeline follows:

```text
Insurance Policy PDFs
        ↓
PDF Extraction
        ↓
Text Cleaning
        ↓
Structure-Aware Chunking
        ↓
Metadata Generation
        ↓
Embedding Generation
        ↓
Vector Database
        ↓
Hybrid Search
   ┌────┴────┐
   ▼         ▼
Semantic   Keyword
 Search     Search
   └────┬────┘
        ▼
   Candidate Results
        ↓
   Relevance Ranking
        ↓
   Relevant Evidence
        ↓
   LLM / Agent
```

---

## 🧠 Multi-Agent Workflow

The system uses a stateful **LangGraph workflow**.

```text
                  User Request
                       │
                       ▼
                Orchestrator
                       │
                       ▼
              Document Analyzer
                       │
                       ▼
              Policy Researcher
                       │
                       ▼
               Risk Assessment
                       │
                 ┌─────┴─────┐
                 │           │
             Missing?       Complete
                 │           │
                 ▼           ▼
          Additional      Underwriting
           Retrieval        Decision
                 │           │
                 └─────┬─────┘
                       ▼
                Final Response
```

The workflow allows agents to perform additional retrieval when required information is missing or when the retrieved evidence is insufficient.

---

## 🛠️ Technology Stack

### Programming

* Python 3.10+
* SQL

### Agentic AI

* LangGraph
* LangChain
* Agent workflows
* Tool calling
* Structured outputs
* Multi-agent orchestration

### LLM

The project is designed to support local/open-source models through:

* Ollama
* Hugging Face models

Optional integrations can be added for:

* Google Gemini
* OCI Generative AI

### Retrieval

* ChromaDB
* FAISS
* Sentence Transformers
* Semantic Search
* Keyword Search
* Hybrid Retrieval

### Document Processing

* PyMuPDF
* Unstructured
* PDF text extraction
* Document chunking
* Metadata extraction

### Machine Learning

* Scikit-learn
* XGBoost
* Feature Engineering
* Risk Classification
* Model Evaluation

### Backend

* FastAPI
* REST APIs
* Pydantic
* API validation

### Frontend

* Streamlit

### MLOps / Observability

* MLflow
* Langfuse
* Experiment Tracking
* Model Monitoring
* Agent Observability
* Evaluation Pipelines

### Testing

* Pytest
* Unit Testing
* Integration Testing

### Deployment

* Docker
* Docker Compose
* GitHub Actions

---

## 📁 Project Structure

```text
insure-agent/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
│
├── app/
│   ├── main.py
│   ├── config.py
│   │
│   ├── agents/
│   │   ├── orchestrator.py
│   │   ├── document_analyzer.py
│   │   ├── policy_researcher.py
│   │   ├── risk_assessor.py
│   │   └── underwriter.py
│   │
│   ├── rag/
│   │   ├── ingestion.py
│   │   ├── chunking.py
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   ├── hybrid_search.py
│   │   └── reranker.py
│   │
│   ├── models/
│   │   ├── risk_model.py
│   │   └── schemas.py
│   │
│   ├── tools/
│   │   ├── policy_search.py
│   │   ├── calculator.py
│   │   └── customer_lookup.py
│   │
│   ├── guardrails/
│   │   ├── pii.py
│   │   ├── validation.py
│   │   └── prompt_injection.py
│   │
│   ├── evaluation/
│   │   ├── rag_eval.py
│   │   ├── agent_eval.py
│   │   └── datasets.py
│   │
│   └── api/
│       └── routes.py
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
│   ├── policies/
│   └── sample_customers/
│
├── tests/
│   ├── test_agents.py
│   ├── test_rag.py
│   ├── test_risk_model.py
│   ├── test_api.py
│   └── test_guardrails.py
│
├── scripts/
│   ├── ingest_documents.py
│   └── evaluate.py
│
└── .github/
    └── workflows/
        └── ci.yml
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/insure-agent.git
cd insure-agent
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file based on `.env.example`.

```env
LLM_PROVIDER=ollama
LLM_MODEL=<local-model-name>

VECTOR_DB=chroma

EMBEDDING_MODEL=<embedding-model>

API_HOST=0.0.0.0
API_PORT=8000
```

Optional cloud model configuration can be added later.

### 5. Start the Application

```bash
streamlit run frontend/streamlit_app.py
```

For the API:

```bash
uvicorn app.main:app --reload
```

---

## 🧪 Testing

Run the test suite using:

```bash
pytest
```

Tests cover:

* Agent workflow
* Policy retrieval
* Risk scoring
* API validation
* Guardrails
* Input validation
* Failure handling

---

## 📊 Evaluation

Insure-Agent includes an evaluation framework for measuring both RAG and agent performance.

### RAG Metrics

* Retrieval Precision
* Retrieval Recall
* Context Relevance
* Citation Accuracy
* Answer Relevance
* Faithfulness

### Agent Metrics

* Task Success Rate
* Tool-Call Success Rate
* Workflow Completion Rate
* Agent Failure Rate
* Average Latency

### Safety Metrics

* Hallucination Rate
* Unsupported Recommendation Rate
* Prompt Injection Detection
* PII Detection

Evaluation results are tracked to compare changes across model, prompt, retrieval, and agent versions.

---

## 🛡️ Responsible AI

Insurance underwriting is a high-impact decision-support use case.

Therefore, the system is designed with the following principles:

* Human review before final decisions
* Evidence-based recommendations
* Policy citation requirements
* No unsupported underwriting claims
* PII protection
* Auditability
* Transparent risk factors
* Model monitoring
* Bias and performance monitoring
* Clear separation between AI recommendations and final business decisions

The system does **not** make autonomous final insurance decisions.

---

## 🔐 Security Considerations

The project includes security controls for:

* Sensitive customer information
* PII detection
* Input validation
* Prompt injection
* Unauthorized tool usage
* API validation
* Secrets management
* Environment-variable configuration

API keys and credentials should never be committed to GitHub.

---

## 🐳 Docker

Build the container:

```bash
docker build -t insure-agent .
```

Run the application:

```bash
docker run -p 8000:8000 insure-agent
```

Docker Compose can be used to run the application together with supporting services.

---

## 🔄 CI/CD

GitHub Actions is used to automate:

```text
Git Push
   ↓
Code Quality Checks
   ↓
Unit Tests
   ↓
Integration Tests
   ↓
Docker Build
   ↓
Deployment
```

The CI pipeline helps ensure that changes are tested before being merged or deployed.

---

## 📈 Future Enhancements

Planned improvements include:

* Graph database integration for relationship-based risk analysis
* Advanced reranking models
* Agent memory
* Model Context Protocol (MCP) tools
* Real-time underwriting data ingestion
* Advanced AgentOps dashboards
* Automated model retraining
* Bias monitoring
* Model drift detection
* Cloud deployment
* Kubernetes deployment
* Human approval workflows
* Advanced risk prediction models

---

## ⚠️ Disclaimer

This project is an **educational and portfolio demonstration** of Agentic AI, RAG, and machine learning engineering techniques.

It does not provide financial, medical, legal, or insurance advice and should not be used to make real-world insurance underwriting decisions.

All example customer data should be synthetic or publicly available and must not contain real personally identifiable information.

---

## 👨‍💻 Author

**Sri Harshitha Anugu**

Generative AI Engineer | Data Scientist | Agentic AI Engineer | Machine Learning Engineer

---

## 📄 License

This project is licensed under the **MIT License**.
