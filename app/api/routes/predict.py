"""
Prediction route.
Accepts a CSV file, runs the full pipeline:
  1. Parse CSV
  2. Enrich with weather columns
  3. Run model inference
Returns the enriched + predicted dataframe as a CSV file response.
"""
import io
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse

from app.services.csv_service import parse_uploaded_csv
from app.services.weather_service import enrich_with_weather
from app.services.inference_service import run_inference

router = APIRouter()


@router.post("/predict-csv", summary="Run prediction pipeline and return enriched CSV")
async def predict_csv(file: UploadFile = File(...)) -> StreamingResponse:
    if not file.filename or not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only .csv files are accepted.")

    contents = await file.read()

    # Step 1 – parse
    df = parse_uploaded_csv(contents, return_dataframe=True)

    # Step 2 – weather enrichment
    df = enrich_with_weather(df)

    # Step 3 – inference
    df = run_inference(df)

    # Return as CSV download
    output = io.StringIO()
    df.to_csv(output, index=False)
    output.seek(0)

    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=predicted_output.csv"},
    )
