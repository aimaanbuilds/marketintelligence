from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from app.routes.analyze import router

app = FastAPI(
    title="Market Intelligence API"
)

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {
        "status": "running"
    }