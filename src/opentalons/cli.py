from __future__ import annotations

import argparse
import json

from opentalons.models import TaskRequest
from opentalons.orchestrator import Orchestrator


def main() -> None:
    parser = argparse.ArgumentParser(description="OpenTalons CLI")
    parser.add_argument("goal", help="Goal to execute")
    parser.add_argument("--context", default=None, help="Optional context")
    args = parser.parse_args()

    orchestrator = Orchestrator()
    result = orchestrator.run(TaskRequest(goal=args.goal, context=args.context))
    payload = {
        "goal": result.goal,
        "provider": result.provider,
        "plan": {"summary": result.plan.summary, "steps": result.plan.steps},
        "output": result.output,
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
