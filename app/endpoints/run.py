from fastapi import APIRouter, Query
from ..models.run import Run

from ..db import db


run_router = APIRouter()


@run_router.get('/run', tags=['run'])
async def get_runs(room_id: str = Query(default=None), user_id: str = Query(default=None)):
    runs = list(db.runs.find())
    for run in runs:
        run['_id'] = None

    return runs


@run_router.post('/run', tags=['run'])
async def create_run(run: Run):
    db.runs.insert_one(run.dict())
