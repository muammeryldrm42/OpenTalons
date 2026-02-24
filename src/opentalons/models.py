from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass(frozen=True)
class TaskRequest:
    goal: str
    context: str | None = None

    def __post_init__(self) -> None:
        if len(self.goal.strip()) < 3:
            raise ValueError("goal must have at least 3 characters")


@dataclass(frozen=True)
class TaskPlan:
    summary: str
    steps: list[str]


@dataclass(frozen=True)
class ToolCall:
    tool_name: str
    arguments: dict[str, str]


@dataclass(frozen=True)
class TaskResult:
    goal: str
    plan: TaskPlan
    output: str
    provider: str
    tool_calls: list[ToolCall] = field(default_factory=list)


@dataclass
class TaskRecord:
    task_id: str
    request: TaskRequest
    status: TaskStatus = TaskStatus.PENDING
    result: TaskResult | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    error: str | None = None

    def touch(self) -> None:
        self.updated_at = datetime.now(timezone.utc)
