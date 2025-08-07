from fastapi import FastAPI
from api.generate import router as generate_router

app = FastAPI()

# Register your endpoint
app.include_router(generate_router)

# Optional root
@app.get("/")
def home():
    return {"message": "RoastMyAd API is running."}
