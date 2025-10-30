import os
from pydantic import BaseModel

class Settings(BaseModel):
    BACKEND_HOST: str = os.getenv('BACKEND_HOST', '0.0.0.0')
    BACKEND_PORT: int = int(os.getenv('BACKEND_PORT', '8000'))
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'postgresql+asyncpg://postgres:postgres@db:5432/rentmini')
    JWT_SECRET: str = os.getenv('JWT_SECRET', 'change_me')

settings = Settings()
