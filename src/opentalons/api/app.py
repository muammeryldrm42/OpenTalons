from __future__ import annotations

from dataclasses import asdict

from opentalons.models import TaskRecord, TaskRequest
from opentalons.orchestrator import Orchestrator


class OpenTalonsAPI:
    """Application service layer used by CLI and future HTTP adapters."""

    def __init__(self, orchestrator: Orchestrator | None = None) -> None:
        self.orchestrator = orchestrator or Orchestrator()

    def health(self) -> dict[str, str]:
        return {"status": "ok"}

    def create_task(self, goal: str, context: str | None = None) -> dict[str, object]:
        record = self.orchestrator.submit(TaskRequest(goal=goal, context=context))
        return self._serialize_record(record)

    def execute_task(self, task_id: str) -> dict[str, object]:
        record = self.orchestrator.run_task(task_id)
        return self._serialize_record(record)

    def list_tasks(self) -> list[dict[str, object]]:
        return [self._serialize_record(task) for task in self.orchestrator.store.list_tasks()]

    def get_task(self, task_id: str) -> dict[str, object]:
        record = self.orchestrator.store.get_task(task_id)
        return self._serialize_record(record)

    def run_goal(self, goal: str, context: str | None = None) -> dict[str, object]:
        return asdict(self.orchestrator.run(TaskRequest(goal=goal, context=context)))

    @staticmethod
    def _serialize_record(record: TaskRecord) -> dict[str, object]:
        data = asdict(record)
        data["status"] = record.status.value
        data["created_at"] = record.created_at.isoformat()
        data["updated_at"] = record.updated_at.isoformat()
        return data


api = OpenTalonsAPI()
