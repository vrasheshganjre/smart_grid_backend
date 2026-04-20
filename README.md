# smart_grid_backend

FastAPI backend template for smart-grid CSV model inferencing with weather enrichment.
This backend serves as the API layer for the sibling `smart_grid_frontend` application.

---

## Project Structure

```
app/
├── main.py                  # App factory, router registration, CORS
├── core/
│   └── config.py            # Typed settings via pydantic-settings
├── api/routes/
│   ├── health.py            # GET /health
│   ├── upload.py            # POST /api/v1/upload-csv
│   └── predict.py           # POST /api/v1/predict-csv
├── schemas/
│   ├── upload.py            # UploadResponse model
│   └── predict.py           # PredictRequest / PredictResponse models
├── services/
│   ├── csv_service.py       # CSV parsing (stub)
│   ├── weather_service.py   # Weather enrichment (stub)
│   └── inference_service.py # Model inference (stub)
├── clients/
│   └── weather_client.py    # Provider-agnostic weather HTTP client (stub)
└── models/
    └── model_adapter.py     # Model load/predict interface (stub)
tests/
├── test_routes.py
├── test_csv_service.py
├── test_weather_service.py
└── test_inference_service.py
```

## Request Flow

```
POST /api/v1/predict-csv
  │
  ├─ 1. Parse CSV bytes → DataFrame         (csv_service)
  ├─ 2. Enrich with weather columns         (weather_service → weather_client)
  ├─ 3. Run model inference                 (inference_service → model_adapter)
  └─ 4. Stream enriched DataFrame as CSV
```

---

## Setup

### Prerequisites

- Python 3.12+
- Docker & Docker Compose (for containerised dev)

### Local run

```bash
# 1. Clone and enter the repo
git clone <repo-url> && cd smart_grid_backend

# 2. Create and activate a virtual environment
python -m venv .venv && source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env and fill in WEATHER_API_KEY, MODEL_PATH, etc.

# 5. Start the server (with hot-reload)
uvicorn app.main:app --reload
```

API docs available at http://localhost:8000/docs

### Docker run

```bash
# Build and start (hot-reload via volume mount)
docker compose up --build

# Stop
docker compose down
```

### Test run

```bash
pytest tests/ -v
```

---

## Implementation TODOs

| Layer | File | What to implement |
|---|---|---|
| Weather client | `app/clients/weather_client.py` | Choose provider, implement `get_weather_for_timestamps` |
| Weather service | `app/services/weather_service.py` | Merge weather data into DataFrame |
| Model adapter | `app/models/model_adapter.py` | Implement `load` and `predict` |
| Inference service | `app/services/inference_service.py` | Select features, call adapter, append predictions |
| CSV service | `app/services/csv_service.py` | Add schema validation and data-quality checks |
