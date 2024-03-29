import pydantic_settings
from typing import Optional


class PlaywrightConfig(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_prefix="QA_PLAYWRIGHT_", env_file=".env", frozen=True, extra="ignore"
    )

    browser: str = ""
    headless: bool = True
    navigation_timeout_sec: int = 120
    elements_timeout_sec: int = 60
    tracing_enable: bool = False
    tracing_screenshots: bool = True
    tracing_snapshots: bool = True


class EnvConfig(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_prefix="QA_ENV_", env_file=".env", frozen=True, extra="ignore"
    )

    artifacts_dir: str = "artifacts/"
    artifacts_remove_old: bool = True
    url_ui: Optional[str] = None