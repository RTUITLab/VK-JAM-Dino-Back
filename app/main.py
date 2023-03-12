from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db import db
# from .endpoints.run_session import run_router
from .endpoints.run import run_router
from .endpoints.user import user_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["dino.rtuitlab.dev", "temp.rtuitlab.dev", "temp1.rtuitlab.dev"],
    # allow_credentials=True,
    allow_methods=["GET","POST","OPTIONS"],
    allow_headers=["*"],
)

app.include_router(run_router)
app.include_router(user_router)
