from fastapi import APIRouter, WebSocket
from uuid import uuid1
from random import Random


current_room = uuid1()
room_size = 2
rand = Random(300)

runs = dict()
runs[current_room] = []

connections = dict()

run_router = APIRouter()


async def start_run(room_id):
    for user in runs[room_id]:
        await connections[user["conn"]]["conn"].send_json({"action": "start", "body": {"seed": rand.randint(1, 900)}})


@run_router.websocket('/run')
async def connect_to_run(connection: WebSocket):
    global current_room
    await connection.accept()
    connection_id = uuid1()
    connections[connection_id] = {"conn": connection, "room": current_room}

    runs[current_room].append(
        {"conn": connection_id, "score": 0, "alive": True})
    if (len(runs[current_room]) >= room_size):
        await start_run(current_room)
        current_room = uuid1()

    try:
        while True:
            data = await connection.receive_text()

        #     for i in range(len(runs['1'])):
        #         await runs['1'][i].send_text(f"Message text was: {data}")
    except Exception as e:
        pass
