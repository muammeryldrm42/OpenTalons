from opentalons.providers.base import Provider
from opentalons.providers.mock import MockProvider


def get_provider(name: str) -> Provider:
    providers: dict[str, Provider] = {
        "mock": MockProvider(),
    }
    try:
        return providers[name]
    except KeyError as exc:
        raise ValueError(f"Unknown provider: {name}") from exc
