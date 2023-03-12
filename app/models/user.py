from pydantic import BaseModel

class Item(BaseModel):
    name: str

class User(BaseModel):
    uid: str
    name: str
    rating: int = 0
    best_score: int = 0
    win_streak: int = 0
    items: list[Item] = []

