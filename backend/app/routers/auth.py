from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import SessionLocal
from app.models.user import User
from app.core.security import create_token

router = APIRouter(prefix='/api/auth', tags=['auth'])

async def get_db():
    async with SessionLocal() as s: yield s

@router.post('/login-telegram')
async def login_telegram(telegram_id: int, role: str = 'seeker', db: AsyncSession = Depends(get_db)):
    if role not in ('seeker','realtor','admin'):
        raise HTTPException(400, 'invalid role')
    res = await db.execute(select(User).where(User.telegram_id==telegram_id))
    user = res.scalar_one_or_none()
    if not user:
        user = User(telegram_id=telegram_id, role=role)
        db.add(user)
        await db.commit()
        await db.refresh(user)
    token = create_token(user.id, user.role)
    return {'id': user.id, 'telegram_id': user.telegram_id, 'role': user.role, 'token': token}
