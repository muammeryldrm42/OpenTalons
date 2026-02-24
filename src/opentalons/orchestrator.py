from __future__ import annotations

from opentalons.config import settings
from opentalons.models import TaskRequest, TaskResult
from opentalons.providers import get_provider
from opentalons.providers.base import Provider


class Orchestrator:
    """Coordinates planning and execution for a task."""

    def __init__(self, provider: Provider | None = None) -> None:
        self.provider = provider or get_provider(settings.default_provider)

    def run(self, request: TaskRequest) -> TaskResult:
        plan = self.provider.build_plan(request)
        output = self.provider.execute(request, plan)
        return TaskResult(
            goal=request.goal,
            plan=plan,
            output=output,
            provider=self.provider.name,
        )
