from __future__ import annotations

from opentalons.models import TaskRequest, TaskResult
from opentalons.orchestrator import Orchestrator

orchestrator = Orchestrator()


def health() -> dict[str, str]:
    return {"status": "ok"}


def run_task(goal: str, context: str | None = None) -> TaskResult:
    return orchestrator.run(TaskRequest(goal=goal, context=context))
