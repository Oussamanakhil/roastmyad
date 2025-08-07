from fastapi import APIRouter
from pydantic import BaseModel
from .roastiq import compute_roastiq
from services.supabase_client import insert_roast  # ✅ Import Supabase insert function

router = APIRouter()

class RoastRequest(BaseModel):
    caption: str
    transcript: str

@router.post("/generate")
def generate_roast_endpoint(req: RoastRequest):
    # 1. Generate roast + scores
    result = compute_roastiq(req.caption, req.transcript)

    # 2. Merge with input to insert in DB
    supabase_payload = {
        **result,
        "caption": req.caption,
        "transcript": req.transcript
    }

    # 3. Insert into Supabase
    insert_response = insert_roast(supabase_payload)

    # 4. Return everything
    return {
        "roast_data": result,
        "inserted": insert_response
    }
