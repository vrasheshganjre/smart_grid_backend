"""
Route-level integration tests using FastAPI's TestClient.

TODO: add test cases for each route as the implementation matures.
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_upload_csv_rejects_non_csv():
    """Non-.csv uploads must be rejected with 400."""
    response = client.post(
        "/api/v1/upload-csv",
        files={"file": ("data.txt", b"col1,col2\n1,2", "text/plain")},
    )
    assert response.status_code == 400


def test_upload_csv_accepts_valid_csv():
    """Valid CSV upload must return filename, row count, and column list."""
    csv_bytes = b"timestamp,power_kw\n2024-01-01 00:00,100\n2024-01-01 01:00,120"
    response = client.post(
        "/api/v1/upload-csv",
        files={"file": ("data.csv", csv_bytes, "text/csv")},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["filename"] == "data.csv"
    assert body["rows"] == 2
    assert "timestamp" in body["columns"]


# TODO: add test_predict_csv_returns_csv_response once inference is implemented
# TODO: add test for invalid CSV structure (missing required columns)
# TODO: add test for empty CSV file
