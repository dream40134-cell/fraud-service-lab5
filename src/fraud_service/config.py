"""Typed, fail-fast configuration. One place to read every environment
variable — never scatter os.environ["X"] across the codebase.
"""
from pathlib import Path

from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="FRAUD_",
        env_file=".env",
        extra="forbid",
    )

    model_path: Path = Field(
        default=Path("models/fraud_model.joblib"),
        description="Path to the joblib model bundle",
    )
    block_threshold: float = Field(
        0.85, ge=0.5, le=0.99,
        description="Risk-approved block threshold",
    )
    log_level: str = Field("INFO")
    git_sha: str = Field("dev")
    registry_token: SecretStr | None = Field(None)

    @field_validator("model_path")
    @classmethod
    def model_file_must_exist(cls, v: Path) -> Path:
        if not v.exists():
            raise ValueError(f"model artefact not found: {v}")
        return v


settings = Settings()
