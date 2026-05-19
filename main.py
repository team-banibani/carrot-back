from fastapi import FastAPI
import uvicorn

from core.config import settings
from api.v1.router import api_router

app = FastAPI(title=settings.APP_NAME)

app.include_router(api_router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
