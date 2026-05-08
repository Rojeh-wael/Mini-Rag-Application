from fastapi import FastAPI, APIRouter,Depends,UploadFile, File,status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
import os
from helpers.config import get_settings, Settings
from controllers import DataController


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)


@data_router.post("/upload/{project_id}") ## Tenets 
async def upload_data(project_id: str, file: UploadFile,
                      app_settings: Settings =Depends(get_settings)):
    # validate file type and properties
    data_controller = DataController()
    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)
    return {"signal": result_signal}