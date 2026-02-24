from __future__ import annotations

from opentalons.models import TaskPlan, TaskRequest
from opentalons.providers.base import Provider


class MockProvider(Provider):
    name = "mock"

    def build_plan(self, request: TaskRequest) -> TaskPlan:
        context_line = f" in context: {request.context}" if request.context else ""
        return TaskPlan(
            summary=f"Plan for '{request.goal}'{context_line}",
            steps=[
                "Clarify objective and constraints",
                "Break objective into actionable milestones",
                "Produce concise execution strategy",
            ],
        )

    def execute(self, request: TaskRequest, plan: TaskPlan) -> str:
        bullets = "\n".join(f"- {step}" for step in plan.steps)
        return (
            f"Goal: {request.goal}\n"
            f"Summary: {plan.summary}\n"
            "Execution outline:\n"
            f"{bullets}\n"
            "Recommendation: start with milestone #1 and measure outcomes weekly."
        )
