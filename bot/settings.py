from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    token: str
    admins: list
    url_helper: str
    url_forum: str

settings = Settings()
