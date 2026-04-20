"""
Unit tests for the CSV service.

TODO: add tests for edge cases as the service is implemented.
"""
import pytest
from app.services.csv_service import parse_uploaded_csv


def test_parse_returns_metadata():
    csv_bytes = b"timestamp,power_kw\n2024-01-01 00:00,100\n2024-01-01 01:00,120"
    result = parse_uploaded_csv(csv_bytes)
    assert result["rows"] == 2
    assert "timestamp" in result["columns"]
    assert "power_kw" in result["columns"]


def test_parse_returns_dataframe():
    csv_bytes = b"timestamp,power_kw\n2024-01-01 00:00,100"
    df = parse_uploaded_csv(csv_bytes, return_dataframe=True)
    assert len(df) == 1
    assert list(df.columns) == ["timestamp", "power_kw"]


# TODO: test_parse_raises_on_empty_file
# TODO: test_parse_raises_on_missing_required_columns
