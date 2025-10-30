from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import SessionLocal
from app.models.user import User
from app.deps.auth import current_user, require_role

router = APIRouter(prefix='/api/realtors', tags=['realtors'])

async def get_db():
    async with SessionLocal() as s: yield s

@router.get('/me')
async def me(user=Depends(current_user), db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(User).where(User.id==user['id']))
    u = res.scalar_one_or_none()
    if not u: raise HTTPException(404,'not found')
    return {'id':u.id,'telegram_id':u.telegram_id,'role':u.role,'name':u.name,'country':u.country,'city':u.city,'locale':u.locale,'contact_telegram':u.contact_telegram,'active':u.active}

@router.put('/me')
async def update_me(name: str | None = None, country: str | None = None, city: str | None=None, locale: str | None=None, contact_telegram: str | None=None, user=Depends(current_user), db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(User).where(User.id==user['id']))
    u = res.scalar_one_or_none()
    if not u: raise HTTPException(404,'not found')
    if name is not None: u.name = name
    if country is not None: u.country = country
    if city is not None: u.city = city
    if locale is not None: u.locale = locale
    if contact_telegram is not None: u.contact_telegram = contact_telegram
    await db.commit()
    return {'ok': True}

@router.post('/admin/block')
async def block_realtor(user_id:int, block: bool = True, admin=Depends(await require_role('admin')), db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(User).where(User.id==user_id))
    u = res.scalar_one_or_none()
    if not u: raise HTTPException(404,'not found')
    u.active = not block
    await db.commit()
    return {'ok': True, 'active': u.active}
