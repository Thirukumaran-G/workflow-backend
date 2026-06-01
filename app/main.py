from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import items

app = FastAPI(title="Backend API", version="1.0.0")

# CORS — allow your frontend domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://storage.googleapis.com",
        "https://YOUR_CDN_DOMAIN",
        "http://localhost:5173",   # local dev
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router, prefix="/api")

@app.get("/health")
async def health():
    return {"status": "ok", "version": "1.0.0"}