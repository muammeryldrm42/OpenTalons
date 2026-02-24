from __future__ import annotations

from collections.abc import Iterable
from uuid import uuid4

from opentalons.models import TaskRecord, TaskRequest


class TaskStore:
    """In-memory task store with OpenClaw-like task lifecycle primitives."""

    def __init__(self) -> None:
        self._tasks: dict[str, TaskRecord] = {}

    def create_task(self, request: TaskRequest) -> TaskRecord:
        task_id = str(uuid4())
        record = TaskRecord(task_id=task_id, request=request)
        self._tasks[task_id] = record
        return record

    def get_task(self, task_id: str) -> TaskRecord:
        try:
            return self._tasks[task_id]
        except KeyError as exc:
            raise ValueError(f"Task not found: {task_id}") from exc

    def list_tasks(self) -> Iterable[TaskRecord]:
        return self._tasks.values()
