from opentalons.api.app import OpenTalonsAPI
from opentalons.config import Settings
from opentalons.models import TaskRequest, TaskStatus
from opentalons.orchestrator import Orchestrator
from opentalons.providers import resolve_provider


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


def test_resolve_provider_fallback_for_invalid_name() -> None:
    provider, provider_name = resolve_provider("nonexistent-provider", fallback="mock")
    assert provider.name == "mock"
    assert provider_name == "mock"


def test_orchestrator_handles_blank_default_provider_config() -> None:
    orchestrator = Orchestrator(runtime_settings=Settings(default_provider="   "))
    assert orchestrator.provider_name == "mock"


def test_health_includes_resolved_provider_and_available_providers() -> None:
    api = OpenTalonsAPI()
    health = api.health()
    assert health["status"] == "ok"
    assert "mock" in health["available_providers"]
    assert health["provider"] == "mock"
