from .settings import Settings
from pymongo import MongoClient


settings = Settings()
client = MongoClient(settings.mongo_url)
db = client['dino']

__all__ = [db]
