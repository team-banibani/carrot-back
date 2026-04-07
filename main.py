from fastapi import FastAPI

from api.v1.router import api_router
from core.config import settings

app = FastAPI(title=settings.APP_NAME)

app.include_router(api_router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    return {"status": "ok"}
