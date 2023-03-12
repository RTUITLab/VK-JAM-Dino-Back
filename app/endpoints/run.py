from fastapi import APIRouter, Query
from ..models.run import Run

from ..db import db


run_router = APIRouter()

@run_router.get('/run')
async def get_runs(room_id: str = Query(default=None), user_id: str = Query(default=None)):
    pass

@run_router.post('/run')
async def create_run(run: Run):
    db.runs.insert_one(run.dict())
