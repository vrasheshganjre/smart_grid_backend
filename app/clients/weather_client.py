"""
Weather API client abstraction.
Decouples the service layer from any specific weather provider.
Swap the implementation here without touching service code.
"""
from typing import Any
import httpx

from app.core.config import settings


class WeatherClient:
    """
    Provider-agnostic HTTP client for fetching weather data.

    TODO:
        - Choose a weather provider (e.g. Open-Meteo, OpenWeatherMap, Visual Crossing).
        - Implement get_weather_for_timestamps() with real API calls.
        - Add retry logic, timeout handling, and rate-limit awareness.
        - Cache repeated calls for the same timestamp/location window.
    """

    def __init__(self) -> None:
        self.base_url = settings.WEATHER_API_BASE_URL
        self.api_key = settings.WEATHER_API_KEY

    async def get_weather_for_timestamps(
        self,
        timestamps: list[str],
        location: str,
    ) -> list[dict[str, Any]]:
        """
        Fetch weather observations for a list of timestamps at a given location.

        Args:
            timestamps: ISO-8601 datetime strings matching the dataset rows.
            location: Human-readable or lat/lon location string.

        Returns:
            List of dicts, one per timestamp, with weather field keys.

        TODO: implement real HTTP call using httpx.AsyncClient
        """
        raise NotImplementedError("WeatherClient.get_weather_for_timestamps is not yet implemented.")
