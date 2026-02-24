from __future__ import annotations

from dataclasses import dataclass


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
class TaskResult:
    goal: str
    plan: TaskPlan
    output: str
    provider: str
