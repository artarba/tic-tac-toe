import logging

import uvicorn
from fastapi import APIRouter, FastAPI

from apps.recognition.routers import recognition_router


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = FastAPI()
api_v1 = APIRouter()

api_v1.include_router(recognition_router, prefix="/recognition")
app.include_router(api_v1, prefix="/api")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, ws_ping_interval=10, ws_ping_timeout=10)