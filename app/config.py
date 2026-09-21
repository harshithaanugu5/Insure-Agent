from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


def env_value(name: str, default: str) -> str:
    return os.getenv(name) or default


@dataclass
class Settings:
    app_name: str = "Insure Agent"
    api_host: str = env_value("API_HOST", "0.0.0.0")
    api_port: int = int(env_value("API_PORT", "8000"))
    llm_provider: str = env_value("LLM_PROVIDER", "ollama")
    llm_model: str = env_value("LLM_MODEL", "llama3")
    vector_db: str = env_value("VECTOR_DB", "chroma")
    embedding_model: str = env_value("EMBEDDING_MODEL", "all-MiniLM-L6-v2")


settings = Settings()
