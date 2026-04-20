"""
Weather enrichment service.
Adds weather-derived columns to the power dataset DataFrame before inferencing.
"""
import pandas as pd

from app.clients.weather_client import WeatherClient


def enrich_with_weather(df: pd.DataFrame) -> pd.DataFrame:
    """
    Enrich the power dataset with weather columns.

    Expected new columns (illustrative — adjust to model requirements):
        - temperature_c
        - humidity_pct
        - wind_speed_kmh
        - cloud_cover_pct
        - weather_condition

    Args:
        df: Raw power dataset DataFrame, expected to contain a datetime column.

    Returns:
        DataFrame with appended weather columns.

    TODO:
        - Identify the datetime and location columns in the dataset.
        - Call WeatherClient.get_weather_for_timestamps() with those values.
        - Merge returned weather data on datetime / location keys.
        - Handle missing weather data gracefully (impute or raise).
    """
    # Placeholder — returns df unchanged until implemented
    client = WeatherClient()  # noqa: F841  TODO: use client to fetch weather data
    return df
