from fastapi import APIRouter
from pydantic import BaseModel
from .roastiq import compute_roastiq

router = APIRouter()

class RoastRequest(BaseModel):
    caption: str
    transcript: str

@router.post("/generate")
def generate_roast_endpoint(req: RoastRequest):
    result = compute_roastiq(req.caption, req.transcript)
    return result
