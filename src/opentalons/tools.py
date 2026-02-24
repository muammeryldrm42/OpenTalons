from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ToolSpec:
    name: str
    description: str


class ToolRegistry:
    """Simple built-in tool catalog for plan post-processing."""

    def __init__(self) -> None:
        self._tools: dict[str, ToolSpec] = {
            "checklist": ToolSpec("checklist", "Turn plan steps into an operator checklist"),
            "risk_scan": ToolSpec("risk_scan", "Generate baseline risks for a goal"),
        }

    def list_tools(self) -> list[ToolSpec]:
        return list(self._tools.values())

    def has_tool(self, name: str) -> bool:
        return name in self._tools

    def run_tool(self, name: str, payload: dict[str, str]) -> str:
        if name == "checklist":
            steps = payload.get("steps", "")
            return "\n".join(f"[ ] {line.strip('- ').strip()}" for line in steps.splitlines() if line.strip())
        if name == "risk_scan":
            goal = payload.get("goal", "")
            return (
                f"Risk scan for '{goal}':\n"
                "- scope creep\n"
                "- dependency delays\n"
                "- weak success metrics"
            )
        raise ValueError(f"Unknown tool: {name}")
