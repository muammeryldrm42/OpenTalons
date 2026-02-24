from __future__ import annotations

import argparse
import json

from opentalons.api.app import OpenTalonsAPI


def main() -> None:
    parser = argparse.ArgumentParser(description="OpenTalons CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run goal instantly")
    run_parser.add_argument("goal")
    run_parser.add_argument("--context", default=None)

    create_parser = subparsers.add_parser("create", help="Create async-like task")
    create_parser.add_argument("goal")
    create_parser.add_argument("--context", default=None)

    exec_parser = subparsers.add_parser("execute", help="Execute task by id")
    exec_parser.add_argument("task_id")

    subparsers.add_parser("list", help="List all tasks")

    get_parser = subparsers.add_parser("get", help="Get task details")
    get_parser.add_argument("task_id")

    args = parser.parse_args()
    api = OpenTalonsAPI()

    if args.command == "run":
        payload = api.run_goal(goal=args.goal, context=args.context)
    elif args.command == "create":
        payload = api.create_task(goal=args.goal, context=args.context)
    elif args.command == "execute":
        payload = api.execute_task(task_id=args.task_id)
    elif args.command == "list":
        payload = api.list_tasks()
    else:
        payload = api.get_task(task_id=args.task_id)

    print(json.dumps(payload, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
