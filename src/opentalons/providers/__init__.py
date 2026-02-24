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
    provider_name = (name or "").strip().lower()
    providers = provider_registry()
    try:
        return providers[provider_name]
    except KeyError as exc:
        raise ValueError(f"Unknown provider: {name}") from exc


def resolve_provider(name: str | None, fallback: str = "mock") -> tuple[Provider, str]:
    """Resolve provider safely and return provider + resolved name.

    This function is resilient against empty/invalid config values.
    """
    providers = provider_registry()
    requested = (name or "").strip().lower()
    fallback_name = (fallback or "").strip().lower() or "mock"

    if requested in providers:
        return providers[requested], requested
    if fallback_name in providers:
        return providers[fallback_name], fallback_name
    # defensive fallback for corrupted registry/config
    return MockProvider(), "mock"
