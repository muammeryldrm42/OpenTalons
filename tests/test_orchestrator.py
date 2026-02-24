from opentalons.api.app import OpenTalonsAPI
from opentalons.models import TaskRequest, TaskStatus
from opentalons.orchestrator import Orchestrator


def test_orchestrator_run_produces_steps_and_output() -> None:
    orchestrator = Orchestrator()
    result = orchestrator.run(TaskRequest(goal="Plan launch", context="SaaS"))

    assert result.provider == "mock"
    assert result.plan.steps
    assert "Goal: Plan launch" in result.output
    assert len(result.tool_calls) >= 1


def test_task_lifecycle_create_execute_get() -> None:
    api = OpenTalonsAPI()

    created = api.create_task(goal="Build roadmap", context="AI")
    assert created["status"] == TaskStatus.PENDING.value

    executed = api.execute_task(created["task_id"])
    assert executed["status"] == TaskStatus.COMPLETED.value
    assert executed["result"]["goal"] == "Build roadmap"

    fetched = api.get_task(created["task_id"])
    assert fetched["status"] == TaskStatus.COMPLETED.value


def test_task_request_validation() -> None:
    request = TaskRequest(goal="Build roadmap")
    assert request.goal == "Build roadmap"


from opentalons.providers import resolve_provider


def test_resolve_provider_fallback_for_invalid_name() -> None:
    provider = resolve_provider("nonexistent-provider", fallback="mock")
    assert provider.name == "mock"
