"""
Centralised typed settings loaded from environment variables / .env file.
Add fields here as the project grows; never hard-code secrets.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ── Application ──────────────────────────────────────────────────────────
    APP_NAME: str = "smart-grid-backend"
    APP_ENV: str = "development"  # development | production
    DEBUG: bool = True

    # ── Server ────────────────────────────────────────────────────────────────
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # ── Weather API ───────────────────────────────────────────────────────────
    # TODO: replace with the real weather provider once selected
    WEATHER_API_BASE_URL: str = "https://api.example-weather-provider.com/v1"
    WEATHER_API_KEY: str = ""

    # ── Model ─────────────────────────────────────────────────────────────────
    # TODO: set the path to the trained model artefact
    MODEL_PATH: str = "models/model.pkl"

    # ── CORS ──────────────────────────────────────────────────────────────────
    # Comma-separated allowed origins; adjust for frontend dev server
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:5173"]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


settings = Settings()
