from fastapi import APIRouter, Query, status
from ..db import db


user_router = APIRouter()

@user_router.get('/user')
async def getUser(uid: str = Query(default=None)):
    user = db.users.find_one({ "uid": uid })
    if user != None:
        return status.HTTP_200_OK
    else:
        return status.HTTP_404_NOT_FOUND

