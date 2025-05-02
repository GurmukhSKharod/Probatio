from pydantic import BaseModel

class TestResult(BaseModel):
    strategy: str
    success: bool
    output: str
