from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db import db
from .endpoints.run_session import run_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    print('asdas')
    return {"Hello": 'Dino'}

app.include_router(run_router)
