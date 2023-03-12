from fastapi import APIRouter, Query, status
from ..db import db

from ..models.user import User


user_router = APIRouter()


@user_router.get('/user', response_model=User, tags=['user'])
async def getUser(uid: str = Query(default=None)):
    user = db.users.find_one({"uid": uid})
    user["_id"] = ''
    if user != None:
        return user
    else:
        return status.HTTP_404_NOT_FOUND


@user_router.post('/user', tags=['user'])
async def createUser(user: User):
    user = db.users.find_one({"uid": user.uid})
    if user != None:
        return status.HTTP_400_BAD_REQUEST

    db.users.insert_one(user.dict())

    return status.HTTP_201_CREATED


# @user_router.get('/user?top')
