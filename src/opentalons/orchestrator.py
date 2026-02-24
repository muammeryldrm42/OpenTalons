from __future__ import annotations

from opentalons.config import Settings, settings
from opentalons.models import TaskPlan, TaskRecord, TaskRequest, TaskResult, TaskStatus, ToolCall
from opentalons.providers import resolve_provider
from opentalons.providers.base import Provider
from opentalons.store import TaskStore
from opentalons.tools import ToolRegistry


class Orchestrator:
    """Coordinates planning, execution, and task lifecycle."""

    def __init__(
        self,
        provider: Provider | None = None,
        store: TaskStore | None = None,
        tools: ToolRegistry | None = None,
        runtime_settings: Settings | None = None,
    ) -> None:
        self.settings = runtime_settings or settings
        if provider is None:
            resolved_provider, resolved_name = resolve_provider(self.settings.default_provider, fallback="mock")
            self.provider = resolved_provider
            self.provider_name = resolved_name
        else:
            self.provider = provider
            self.provider_name = provider.name

        self.store = store or TaskStore()
        self.tools = tools or ToolRegistry()

    def submit(self, request: TaskRequest) -> TaskRecord:
        return self.store.create_task(request)

    def run(self, request: TaskRequest) -> TaskResult:
        plan = self.provider.build_plan(request)
        output = self.provider.execute(request, plan)
        tool_calls = self._auto_tool_calls(request, plan)
        return TaskResult(
            goal=request.goal,
            plan=plan,
            output=output,
            provider=self.provider_name,
            tool_calls=tool_calls,
        )

    def run_task(self, task_id: str) -> TaskRecord:
        record = self.store.get_task(task_id)
        record.status = TaskStatus.RUNNING
        record.touch()
        try:
            record.result = self.run(record.request)
            record.status = TaskStatus.COMPLETED
        except Exception as exc:  # noqa: BLE001
            record.status = TaskStatus.FAILED
            record.error = str(exc)
        record.touch()
        return record

    def _auto_tool_calls(self, request: TaskRequest, plan: TaskPlan) -> list[ToolCall]:
        tool_calls: list[ToolCall] = []
        checklist_input = {"steps": "\n".join(f"- {step}" for step in plan.steps)}
        if self.tools.has_tool("checklist"):
            self.tools.run_tool("checklist", checklist_input)
            tool_calls.append(ToolCall(tool_name="checklist", arguments=checklist_input))

        if self.tools.has_tool("risk_scan"):
            risk_input = {"goal": request.goal}
            self.tools.run_tool("risk_scan", risk_input)
            tool_calls.append(ToolCall(tool_name="risk_scan", arguments=risk_input))
        return tool_calls
