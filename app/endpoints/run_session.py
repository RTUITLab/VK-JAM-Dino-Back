from fastapi import APIRouter, WebSocket


runs = dict()

run_router = APIRouter()

@run_router.websocket('/run')
async def connect_to_run(socket: WebSocket):
    await socket.accept()
    while True:
        data = await socket.receive_json()
        await socket.send_text(f"Message text was: {data}")
