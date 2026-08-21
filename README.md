# Bank-Agent: Multi-Agent Insurance Underwriting Assistant

[](https://opensource.org/licenses/MIT)
[](https://www.python.org/downloads/)
[](https://www.google.com/search?q=https://education.oracle.com/oracle-cloud-infrastructure-2025-generative-ai-professional/pP_OCIGENAI2025PRO)

## 📌 Project Overview

**Banc-Agent** is an advanced **Agentic RAG (Retrieval-Augmented Generation)** system designed for the Bancassurance sector. Unlike traditional chatbots, this system utilizes a multi-agent orchestration layer to automate the complex process of insurance policy underwriting and risk assessment.

The system analyzes customer financial data and medical disclosures against bank-partnered insurance policies to provide an automated "Risk Score" and "Preliminary Underwriting Decision."

## 🚀 Key Features

  * **Multi-Agent Orchestration:** Uses **LangGraph** to manage stateful, multi-turn reasoning between a *Document Analyzer Agent* and a *Risk Auditor Agent*.
  * **Intelligent Retrieval:** Implements Hybrid Search (Semantic + Keyword) to parse complex tables and clauses within long-form PDF insurance policies.
  * **Regulatory Guardrails:** Built-in logic to ensure AI responses comply with standard banking disclosure requirements.
  * **Explainable Risk Scoring:** Every decision includes a "Chain of Thought" (CoT) explanation and direct citations from the source policy documents.

## 🛠️ Tech Stack

  * **LLM Orchestration:** LangGraph / LangChain
  * **Generative AI Models:** Gemini 2.0 Flash / OCI Generative AI Service
  * **Vector Database:** ChromaDB (or Pinecone)
  * **PDF Processing:** PyMuPDF / Unstructured.io
  * **UI Framework:** Streamlit
  * **Language:** Python 3.10

## 📁 Project Structure

```text
Banc-Agent-RAG/
├── agents/
│   ├── doc_analyzer.py      # Extracts & summarizes data from policy PDFs
│   └── risk_auditor.py      # Evaluates risk against banking guidelines
├── tools/
│   ├── policy_search.py     # Vector database retrieval tool
│   └── calculator.py        # Logic for premium & risk math
├── data/
│   ├── raw_policies/        # Sample insurance policy PDFs
│   └── vector_store/        # Persisted ChromaDB embeddings
├── graph_workflow.py        # The "Brain" (LangGraph State Machine)
├── app.py                   # Streamlit User Interface
├── requirements.txt         # Dependencies
└── README.md
```

## ⚙️ Installation & Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/Banc-Agent-RAG.git
    cd Banc-Agent-RAG
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file and add your API keys:

    ```env
    GOOGLE_API_KEY=your_gemini_key_here
    # Or OCI Credentials if using OCI GenAI Service
    ```

5.  **Run the application:**

    ```bash
    streamlit run app.py
    ```

## 📊 How it Works (The Workflow)

1.  **Input:** User uploads a customer profile or asks a specific coverage question.
2.  **Analyze:** The *Document Analyzer* retrieves relevant policy segments from the Vector DB.
3.  **Audit:** The *Risk Auditor* checks the retrieved info against predefined underwriting rules.
4.  **Loop:** If the Auditor finds missing info, it sends a request back to the Analyzer for a more specific search.
5.  **Output:** A final underwriting recommendation (Approve/Flag/Decline) with source citations.


**Author:** Sri Harshitha
