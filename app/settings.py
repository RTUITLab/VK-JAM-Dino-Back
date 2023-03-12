from pydantic import BaseSettings


class Settings(BaseSettings):
    mongo_url: str = ''
