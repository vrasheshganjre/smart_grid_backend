from fastapi import APIRouter, status, UploadFile, File
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/upload", summary="Upload CSV route (stub)")
async def upload_stub(file: UploadFile = File(...)):
    if not file.filename or not file.filename.endswith(".csv"):
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": "Only .csv files are accepted."})
    # TODO: Implement CSV upload and validation logic
    return {"route": "upload", "filename": file.filename}
