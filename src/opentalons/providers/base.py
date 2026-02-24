from __future__ import annotations

from abc import ABC, abstractmethod

from opentalons.models import TaskPlan, TaskRequest


class Provider(ABC):
    """Contract implemented by all inference providers."""

    name: str

    @abstractmethod
    def build_plan(self, request: TaskRequest) -> TaskPlan:
        raise NotImplementedError

    @abstractmethod
    def execute(self, request: TaskRequest, plan: TaskPlan) -> str:
        raise NotImplementedError
