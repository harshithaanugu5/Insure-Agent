from __future__ import annotations

from app.rag.ingestion import load_policy_documents


def main() -> None:
    docs = load_policy_documents()
    print(f"Loaded {len(docs)} policy documents.")
    for doc in docs[:3]:
        print(doc)


if __name__ == "__main__":
    main()
