# Project Guidelines

## Scope
- This repository is the backend workspace for a smart grid system.
- The frontend is expected to exist as a sibling directory named `smart_grid_frontend` one level above this repository.
- Current priority is scaffolding only: create or update a clean, modular Python FastAPI template for model inferencing and backend serving.

## Working Mode
- Prefer template and architecture scaffolding over implementation.
- Do not implement model logic, weather API integration logic, or prediction logic unless explicitly requested.
- Create stubs, placeholders, interfaces, and TODO markers where business logic would go.

## Target Backend Purpose
- Accept CSV power dataset uploads.
- Prepare a weather-enrichment step (add weather columns from an external weather API).
- Prepare a model inferencing flow.
- Return predicted data as CSV.
- Keep all inferencing and enrichment flow modular and testable.

## Expected Project Structure
- Use a clean FastAPI service layout similar to:
  - `app/main.py` for application factory and router registration.
  - `app/api/routes/` for route modules.
  - `app/schemas/` for request and response models.
  - `app/services/` for business orchestration (CSV parsing, weather enrichment, inference pipeline).
  - `app/clients/` for external integrations (weather API client abstraction).
  - `app/core/` for configuration and shared settings.
  - `app/models/` for model-loading interfaces or adapters.
  - `tests/` for unit and route-level test placeholders.

## API Route Expectations
- Include route templates for:
  - Health/status check.
  - CSV upload endpoint.
  - Prediction endpoint that returns CSV response.
- Keep route handlers thin; delegate workflow to service layer.

## Configuration And Secrets
- Centralize configuration through environment variables and a typed settings module.
- Keep secrets out of source control.
- Provide sample env file templates when needed (`.env.example`).

## Docker And Local Development
- Always include Docker support when scaffolding this backend:
  - `Dockerfile` suitable for production-style container runs.
  - `docker-compose.yml` for local development workflow.
- Ensure the containerized app can run the FastAPI server consistently in dev and deployment contexts.

## Dependency Management
- Maintain a `requirements.txt` that includes:
  - FastAPI stack.
  - ASGI server.
  - CSV/data handling dependencies.
  - HTTP client for weather API calls.
  - Basic test tooling.
- Keep dependency list explicit and reproducible.

## Documentation And Commands
- When adding scaffolding, update [README.md](README.md) with setup and run instructions.
- Prefer concise command sections for:
  - Local run.
  - Docker run.
  - Test run.

## Collaboration Conventions
- Use small, modular files and clear boundaries between API, service, and integration layers.
- Add brief comments only where flow is non-obvious.
- Avoid broad refactors outside the requested scope.
- If requirements are ambiguous, ask for missing assumptions before implementing logic-heavy components.
