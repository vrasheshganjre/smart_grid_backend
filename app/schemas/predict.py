from pydantic import BaseModel


class PredictRequest(BaseModel):
    """
    Optional metadata that can accompany a predict request.
    Extend with location, date range, or model version hints as needed.
    """
    location: str | None = None  # e.g. "New York, US" — passed to weather enrichment
    model_version: str | None = None  # TODO: used to select model artefact


class PredictResponse(BaseModel):
    """
    Returned when the caller prefers JSON over the CSV StreamingResponse.
    Not used by default; provided as an alternative contract option.
    """
    rows_processed: int
    download_url: str | None = None  # TODO: populate with signed URL or omit
