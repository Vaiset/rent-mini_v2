from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.db import SessionLocal
from app.models.complaint import Complaint
from app.deps.auth import current_user, require_role

router = APIRouter(prefix='/api/complaints', tags=['complaints'])

async def get_db():
    async with SessionLocal() as s: yield s

@router.post('/')
async def create_complaint(listing_id:int, text:str, contact:str|None=None, user=Depends(current_user), db: AsyncSession = Depends(get_db)):
    c = Complaint(listing_id=listing_id, text=text, contact=contact, from_user_id=user['id'] if user else None)
    db.add(c)
    await db.commit()
    await db.refresh(c)
    return {'id': c.id, 'status': c.status}

@router.get('/admin')
async def list_complaints(admin=Depends(await require_role('admin')), db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(Complaint))
    return [ {'id':c.id,'listing_id':c.listing_id,'text':c.text,'contact':c.contact,'status':c.status} for c in res.scalars().all() ]
