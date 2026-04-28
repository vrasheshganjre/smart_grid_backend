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
- [Astral uv](https://docs.astral.sh/uv/)
- (Optional) `pyenv` for managing multiple Python versions

### Local development (preferred)

```bash
# 1. Clone and enter the repo
git clone <repo-url> && cd smart_grid_backend

# 2. Install dependencies and create the project virtualenv
uv sync

# 3. Configure environment
cp .env.example .env
# Edit .env and fill in WEATHER_API_KEY, MODEL_PATH, etc.

# 4. Start the server (with hot-reload)
uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Windows PowerShell:

```powershell
# 1. Clone and enter the repo
git clone <repo-url>
cd smart_grid_backend

# 2. Install dependencies and create the project virtualenv
uv sync

# 3. Configure environment
Copy-Item .env.example .env
# Edit .env and fill in WEATHER_API_KEY, MODEL_PATH, etc.

# 4. Start the server (with hot-reload)
uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

API docs available at http://localhost:8000/docs

### Local tooling and helpers

Prefer using Astral `uv` to manage the project environment and commands. A `Makefile`
is provided with common targets: `venv`, `install`, `run`, `test`, and `clean`.

Run `make` targets (Linux/macOS):

```bash
# create venv using uv
make venv
# sync dependencies from pyproject.toml / uv.lock
make install
# run the API
make run
# run tests
make test
```

On Windows, prefer calling `uv` directly instead of `make`:

```powershell
uv sync
uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
uv run pytest tests -v
```

If you need Python 3.12, install it via your package manager, `pyenv`, or `uv`:

```bash
# install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

#----INSTALL ONLY IF YOU DON'T HAVE PYTHON 3.12 OR HIGHER----
# install Python 3.12 via uv
uv python install 3.12

# Or using pyenv
curl https://pyenv.run | bash
exec $SHELL
pyenv install 3.12.0
pyenv local 3.12.0
```

Windows options:

```powershell
# install uv with winget
winget install --id AstralSoftware.UV

# install Python 3.12 via uv
uv python install 3.12
```

### Astral `uv` commands

The repository uses Astral `uv` directly. Common commands:

```bash
# create/update the environment from uv.lock
uv sync

# run the API with uvicorn inside the project environment
uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# run the test suite
uv run pytest tests -v

# inspect the active environment
uv pip list
```

### Test run

```bash
uv run pytest tests/ -v
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
