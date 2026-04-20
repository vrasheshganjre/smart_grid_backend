---
name: smart-grid-backend-scaffold
description: 'Scaffold a modular Python FastAPI backend template for smart-grid CSV inferencing workflows with weather enrichment placeholders, Docker setup, requirements.txt, and test stubs. Use when creating or refreshing backend structure for collaborative development without implementing business logic.'
argument-hint: 'Optional: target variant or constraints (for example, strict folder names, package choices, or route naming)'
---

# Smart Grid Backend Scaffold

## What This Skill Produces
- A clean, modular FastAPI backend template for collaborative development.
- Placeholder-only flow for CSV upload, weather enrichment stage, model inferencing stage, and CSV output.
- Docker-ready local development and deployment scaffolding.
- Explicit dependency list and test placeholders.

## When To Use
- Starting a new backend for the smart grid project.
- Standardizing backend structure across contributors.
- Re-scaffolding a backend while preserving existing business logic files.

## Guardrails
- Do scaffold architecture and placeholders.
- Do not implement model inference logic.
- Do not implement weather API integration logic.
- Do not implement prediction/business rules unless explicitly requested.
- Keep handlers thin and push orchestration into service interfaces.

## Workflow
1. Confirm project mode and scope.
- Enforce scaffold-only mode.
- Confirm this backend is paired with sibling frontend folder named smart_grid_frontend.

2. Inspect existing customization and docs.
- Read AGENTS.md or .github/copilot-instructions.md if present.
- Read README.md and link existing docs rather than duplicating content.

3. Scaffold modular backend layout.
- Create app/main.py for app bootstrap and router registration.
- Create app/api/routes for health, upload, and predict route templates.
- Create app/schemas for request and response models.
- Create app/services for CSV parsing, weather enrichment, and inference pipeline service stubs.
- Create app/clients for weather API client abstraction.
- Create app/models for model adapter interfaces.
- Create app/core for typed settings and shared config.
- Create tests for route-level and unit-test placeholders.

4. Add runtime and deployment scaffolding.
- Create requirements.txt with FastAPI, ASGI server, CSV/data handling, HTTP client, and test dependencies.
- Create .env.example with non-secret configuration placeholders.
- Create Dockerfile for production-style container execution.
- Create docker-compose.yml for local development.

5. Add placeholder interfaces and TODO markers.
- Add explicit TODO points where weather enrichment, feature engineering, model loading, and inference will be implemented.
- Keep function signatures and contracts clear for team handoff.

6. Update onboarding docs.
- Update README.md with concise local run, Docker run, and test commands.
- Document high-level request flow and where implementation should be added.

7. Validate scaffold quality.
- Ensure imports resolve and modules are discoverable.
- Ensure route modules are registered in main app.
- Ensure docker-compose boots the API service.
- Ensure no secrets are committed.

## Decision Points
- If files already exist: preserve valuable content, patch incrementally, and avoid destructive rewrites.
- If dependency choices are unspecified: pick widely compatible defaults and keep them explicit.
- If weather provider is unspecified: create a provider-agnostic client interface only.
- If model framework is unspecified: create adapter/protocol interfaces only.

## Completion Checklist
- Project structure matches modular FastAPI boundaries.
- Route templates exist for health, CSV upload, and prediction CSV response.
- Service and client layers are scaffolded with placeholders only.
- Dockerfile and docker-compose.yml exist and are coherent.
- requirements.txt is explicit and reproducible.
- README includes local, Docker, and test commands.
- No business logic implementation was added.

## Example Prompts
- Scaffold this repository using smart-grid-backend-scaffold.
- Refresh the backend template but keep existing implementation files intact.
- Create only the Docker and dependency portions from smart-grid-backend-scaffold.
