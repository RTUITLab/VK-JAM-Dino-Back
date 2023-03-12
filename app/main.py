from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db import db
from .endpoints.run_session import run_router
from .endpoints.user import user_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(run_router)
app.include_router(user_router)
