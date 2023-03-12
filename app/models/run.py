from pydantic import BaseModel


class Run(BaseModel):
    room_id: str
    user_id: str
    score: int
    level: int = 0
    seed: str = ''
    killer: str = ''
