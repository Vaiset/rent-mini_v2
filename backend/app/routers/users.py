from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.db import SessionLocal
from app.models.user import User

router = APIRouter(prefix='/api/users', tags=['users'])

async def get_db():
    async with SessionLocal() as s: yield s

@router.get('/')
async def list_users(db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(User))
    return [ {'id':u.id,'telegram_id':u.telegram_id,'role':u.role,'name':u.name} for u in res.scalars().all() ]
