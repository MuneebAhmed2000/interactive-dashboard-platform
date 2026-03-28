from fastapi import WebSocket
import asyncio
from .data_generator import generate_fake_data

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("WebSocket client connected")  # 👈 debug

    try:
        while True:
            data = generate_fake_data()
            await websocket.send_json(data)
            await asyncio.sleep(2)
    except Exception as e:
        print("WebSocket error:", e)