"""
CSV upload route.
Accepts a multipart CSV file, delegates parsing to the CSV service, and returns
a confirmation payload.  Weather enrichment and inferencing happen downstream
in the predict route.
"""
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas.upload import UploadResponse
from app.services.csv_service import parse_uploaded_csv

router = APIRouter()


@router.post("/upload-csv", response_model=UploadResponse, summary="Upload power dataset CSV")
async def upload_csv(file: UploadFile = File(...)) -> UploadResponse:
    if not file.filename or not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only .csv files are accepted.")

    contents = await file.read()
    meta = parse_uploaded_csv(contents)

    return UploadResponse(
        filename=file.filename,
        rows=meta["rows"],
        columns=meta["columns"],
    )
