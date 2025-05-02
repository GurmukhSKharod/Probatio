from fastapi import APIRouter, UploadFile, File, Form
from models.schemas import TestResult
from core.test_runner import run_test_strategy
from utils.file_ops import save_temp_file

router = APIRouter()

@router.post("/upload", response_model=TestResult)
async def upload_file(file: UploadFile = File(...), strategy: str = Form(...)):
    temp_path = save_temp_file(file)
    result = run_test_strategy(temp_path, strategy)
    return result
