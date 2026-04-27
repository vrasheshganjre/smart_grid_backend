"""
Application factory.  Registers all routers and global middleware.
"""

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import health, upload, predict

# ── Logging setup ───────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.DEBUG if settings.DEBUG else logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(settings.APP_NAME)

logger.info(f"Starting {settings.APP_NAME} in {settings.APP_ENV} mode. Debug={settings.DEBUG}")

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ── CORS ──────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ───────────────────────────────────────────────────────────────────

# Modular, collaborative route registration
app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(upload.router, prefix="/api/v1", tags=["upload"])
app.include_router(predict.router, prefix="/api/v1", tags=["predict"])

# Global exception handler for unhandled errors
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi import status

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # TODO: Add more granular exception handling as needed
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": str(exc), "detail": "Internal server error"},
    )

# ── Collaborative Local Dev Notes ─────────────────────────────────────────────
# - Use .env.example for local dev (copy to .env for secrets)
# - Run locally with `uvicorn app.main:app --reload` or via Docker Compose
# - All devs can use Docker or native Python venv; both are supported
# - No production-only code is present; this file is dev-collaboration ready
