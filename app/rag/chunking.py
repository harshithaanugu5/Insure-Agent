from __future__ import annotations


def chunk_text(text: str, chunk_size: int = 400, overlap: int = 80) -> list[str]:
    if not text or not text.strip():
        return []

    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: list[str] = []
    current: list[str] = []
    current_length = 0

    for paragraph in paragraphs:
        if current_length and current_length + len(paragraph) > chunk_size:
            chunks.append(" ".join(current))
            current = [paragraph]
            current_length = len(paragraph)
        else:
            current.append(paragraph)
            current_length += len(paragraph)

    if current:
        chunks.append(" ".join(current))

    if overlap > 0 and len(chunks) > 1:
        merged: list[str] = []
        for index, chunk in enumerate(chunks):
            if index == 0:
                merged.append(chunk)
                continue
            previous = merged[-1]
            overlap_text = " ".join(previous.split()[-overlap:]) if overlap else ""
            merged.append(f"{overlap_text} {chunk}".strip())
        return merged

    return chunks
