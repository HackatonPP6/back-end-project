import uvicorn

from fastapi import Depends, FastAPI, WebSocket
import asyncio
from src.controller.log import LogController
from src.controller.cache import CacheController
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await asyncio.sleep(10)
        mock_message = {"Aws.virginia": "active", "Aws.saoPaulo": "active", "Jira":"Instável", "Oracle.Vinhedo": 'Fora do Ar', 'Oracle.SaoPaulo': 'active' }
        await websocket.send_json(mock_message)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(CacheController.router)
app.include_router(LogController.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")