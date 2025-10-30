import time, jwt
from typing import Literal
from app.core.config import settings

ALGORITHM = 'HS256'

def create_token(user_id:int, role:Literal['seeker','realtor','admin']):
    payload = {'sub': str(user_id), 'role': role, 'iat': int(time.time())}
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=ALGORITHM)

def decode_token(token:str):
    return jwt.decode(token, settings.JWT_SECRET, algorithms=[ALGORITHM])
