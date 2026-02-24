from opentalons.models import TaskRequest
from opentalons.orchestrator import Orchestrator


def test_orchestrator_run_produces_steps_and_output() -> None:
    orchestrator = Orchestrator()
    result = orchestrator.run(TaskRequest(goal="Plan launch", context="SaaS"))

    assert result.provider == "mock"
    assert result.plan.steps
    assert "Goal: Plan launch" in result.output


def test_task_request_validation() -> None:
    request = TaskRequest(goal="Build roadmap")
    assert request.goal == "Build roadmap"
