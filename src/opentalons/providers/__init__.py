from __future__ import annotations

from opentalons.providers.base import Provider
from opentalons.providers.mock import MockProvider


def provider_registry() -> dict[str, Provider]:
    return {
        "mock": MockProvider(),
    }


def list_provider_names() -> list[str]:
    return sorted(provider_registry().keys())


def get_provider(name: str) -> Provider:
    providers = provider_registry()
    try:
        return providers[name]
    except KeyError as exc:
        raise ValueError(f"Unknown provider: {name}") from exc


def resolve_provider(name: str, fallback: str = "mock") -> Provider:
    providers = provider_registry()
    if name in providers:
        return providers[name]
    if fallback in providers:
        return providers[fallback]
    # defensive fallback for corrupted configs
    return MockProvider()
