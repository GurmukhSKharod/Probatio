import os
import tempfile
from fastapi import UploadFile

def save_temp_file(file: UploadFile) -> str:
    suffix = os.path.splitext(file.filename)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix, mode="wb") as f:
        content = file.file.read()
        f.write(content)
        return f.name
