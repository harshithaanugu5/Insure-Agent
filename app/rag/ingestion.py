from __future__ import annotations

from pathlib import Path


def load_policy_documents(folder: str | Path | None = None) -> list[str]:
    base = Path(folder) if folder is not None else Path(__file__).resolve().parents[2] / "data" / "policies"
    docs: list[str] = []

    if not base.exists():
        return [
            "Policy A: Applicants under age 25 require additional verification.",
            "Policy B: Coverage above $750,000 requires enhanced review.",
            "Policy C: Smoking status must be disclosed and may adjust underwriting terms.",
        ]

    for file in sorted(base.glob("*.md")):
        docs.append(file.read_text(encoding="utf-8"))

    if not docs:
        docs = [
            "Policy A: Applicants under age 25 require additional verification.",
            "Policy B: Coverage above $750,000 requires enhanced review.",
            "Policy C: Smoking status must be disclosed and may adjust underwriting terms.",
        ]

    return docs
