# backend/main.py

from fastapi import FastAPI
from api.gpt_roast import router as gpt_router
from api.upload import router as upload_router

app = FastAPI(title="RoastMyAd API")

# Register API routes
app.include_router(gpt_router, prefix="/roast")
app.include_router(upload_router, prefix="/upload")
