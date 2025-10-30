from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.db import SessionLocal
from app.models.listing import Listing

router = APIRouter(prefix='/api/listings', tags=['listings'])

async def get_db():
    async with SessionLocal() as s: yield s

@router.get('/')
async def list_listings(db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(Listing))
    return [ {'id':l.id,'title':l.title,'price':l.price,'realtor_id':l.realtor_id} for l in res.scalars().all() ]

@router.post('/')
async def create_listing(title: str, price: int, realtor_id: int, db: AsyncSession = Depends(get_db)):
    l = Listing(title=title, price=price, realtor_id=realtor_id)
    db.add(l)
    await db.commit()
    await db.refresh(l)
    return {'id':l.id,'title':l.title,'price':l.price,'realtor_id':l.realtor_id}
