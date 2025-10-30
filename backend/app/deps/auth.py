from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.core.security import decode_token

http_bearer = HTTPBearer(auto_error=False)

async def current_user(creds: HTTPAuthorizationCredentials = Depends(http_bearer)):
    if not creds:
        raise HTTPException(401, 'missing token')
    try:
        payload = decode_token(creds.credentials)
        return {'id': int(payload['sub']), 'role': payload.get('role','seeker')}
    except Exception:
        raise HTTPException(401, 'invalid token')

async def require_role(role:str):
    async def _inner(user=Depends(current_user)):
        roles = ['seeker','realtor','admin']
        if roles.index(user['role']) < roles.index(role):
            raise HTTPException(403, 'forbidden')
        return user
    return _inner
