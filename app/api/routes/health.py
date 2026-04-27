from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.requests import Request

router = APIRouter()

@router.get("/health", summary="Server health check")
async def server_health_check():
    return {"route": "server_health", "status": "ok"}

@router.get("/model-health", summary="Model health check")
async def model_health_check():
    # TODO: Implement real model health check
    return {"route": "model_health", "status": "ok"}