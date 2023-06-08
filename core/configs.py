from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from fastapi.templating import Jinja2Templates
from pathlib import Path

class Settings(BaseSettings):
    DB_URL: str = 'postgresql+asyncpg://postgres:123456@localhost:5432/startup'
    DBBaseModel = declarative_base()
    TEMPLATES = Jinja2Templates(directory='templates')
    MEDIA = Path('media')
    AUTH_COOKIE_NAME: str = 'guniversity' # Pode ser qualquer nome para identificar o usuário autenticado no app
    SALTY: str = 'X49VYJMMDpEmG7og-R8vDjcMwBvKWJUbbX2eEfnXFzIlN35aKYg3viF8xBKIVsTdg7QYyGW-UjCKF8MPVY-I0w'

    class Config:
        case_sensitive = True


settings: Settings = Settings()

