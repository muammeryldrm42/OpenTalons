from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = "OpenTalons"
    environment: str = "dev"
    default_provider: str = "mock"


def _normalize(value: str | None, default: str) -> str:
    normalized = (value or "").strip()
    return normalized if normalized else default


def load_settings() -> Settings:
    return Settings(
        app_name=_normalize(os.getenv("OPENTALONS_APP_NAME"), "OpenTalons"),
        environment=_normalize(os.getenv("OPENTALONS_ENVIRONMENT"), "dev"),
        default_provider=_normalize(os.getenv("OPENTALONS_DEFAULT_PROVIDER"), "mock").lower(),
    )


settings = load_settings()
