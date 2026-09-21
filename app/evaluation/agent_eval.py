from __future__ import annotations


def evaluate_agent_task(task_name: str, success: bool) -> dict:
    return {
        "task": task_name,
        "success": success,
        "score": 1.0 if success else 0.0,
    }
