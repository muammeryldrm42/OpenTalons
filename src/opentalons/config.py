from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = "OpenTalons"
    environment: str = "dev"
    default_provider: str = "mock"


def load_settings() -> Settings:
    return Settings(
        app_name=os.getenv("OPENTALONS_APP_NAME", "OpenTalons"),
        environment=os.getenv("OPENTALONS_ENVIRONMENT", "dev"),
        default_provider=os.getenv("OPENTALONS_DEFAULT_PROVIDER", "mock"),
    )


settings = load_settings()
