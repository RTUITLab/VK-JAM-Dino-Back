from fastapi import APIRouter, WebSocket, Query
from uuid import uuid1
from random import Random
from datetime import datetime
from ..db import db


current_room = uuid1()
room_size = 2
rand = Random()

runs = dict()
runs[current_room] = {"users": [], "started": None}

connections = dict()

run_router = APIRouter()


async def start_run(room_id):
    seed = rand.randint(1, 900)
    db.runs.insert_one({
        "room_id": room_id,
        "seed": seed,
        "finished": False
    })
    for user in runs[room_id]["users"]:
        connection = connections[user["conn"]]
        if user["alive"]:
            await connection["conn"].send_json({"action": "start", "body": {"seed": seed}})

    runs[current_room]["started"] = datetime.now()


async def drop_user(room_id, user_id):
    for user in runs[room_id]["users"]:
        connection = connections[user["conn"]]
        if user["alive"]:
            await connection["conn"].send_json({"action": "user_dies", "body": {"id": str(user_id)}})

    runs[current_room]["started"] = datetime.now()


@run_router.websocket('/run')
async def connect_to_run(connection: WebSocket, uid: str = Query(default=None)):
    global current_room
    await connection.accept()
    connection_id = uid
    connections[connection_id] = {"conn": connection, "room": current_room}

    runs[current_room]["users"].append(
        {"conn": connection_id, "score": 0, "alive": True})
    if (len(runs[current_room]["users"]) >= room_size):
        await start_run(current_room)
        current_room = uuid1()
        runs[current_room] = {"users": []}

    try:
        while True:
            data = await connection.receive_json()

            if (data["action"] == "user_dies"):
                user["alive"] = False
                user["reason"] = "DIE"
                room_id = connections[connection_id]["room"]
                await drop_user(room_id, connection_id)
                break

    except Exception as e:
        room_id = connections[connection_id]["room"]

        user = [x for x in runs[room_id]["users"]
                if x["conn"] == connection_id][0]
        if runs[room_id]["started"] == False:
            runs[room_id].remove(user)
        else:
            user["alive"] = False
            user["reason"] = "DISCONNECETD"
            await drop_user(room_id, connection_id)

        del connections[connection_id]
