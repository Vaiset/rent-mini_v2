from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.db import SessionLocal
from app.models.listing import Listing
from app.deps.auth import require_role
import os, shutil

UPLOAD_DIR = '/app/uploads'

router = APIRouter(prefix='/api/listings', tags=['listings'])

async def get_db():
    async with SessionLocal() as s: yield s

@router.get('/')
async def list_listings(db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(Listing))
    return [ {'id':l.id,'title':l.title,'price':l.price,'realtor_id':l.realtor_id,'image_url':l.image_url} for l in res.scalars().all() ]

@router.post('/')
async def create_listing(title: str, price: int, realtor_id: int, db: AsyncSession = Depends(get_db), user=Depends(await require_role('realtor'))):
    l = Listing(title=title, price=price, realtor_id=realtor_id)
    db.add(l)
    await db.commit()
    await db.refresh(l)
    return {'id':l.id,'title':l.title,'price':l.price,'realtor_id':l.realtor_id,'image_url':l.image_url}

@router.post('/upload')
async def upload_image(listing_id:int, file: UploadFile = File(...), db: AsyncSession = Depends(get_db), user=Depends(await require_role('realtor'))):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    ext = os.path.splitext(file.filename)[1]
    fname = f'listing_{listing_id}{ext}'
    path = os.path.join(UPLOAD_DIR, fname)
    with open(path, 'wb') as f:
        shutil.copyfileobj(file.file, f)
    # save url
    res = await db.execute(select(Listing).where(Listing.id==listing_id))
    l = res.scalar_one_or_none()
    if not l: raise HTTPException(404, 'listing not found')
    l.image_url = f'/uploads/{fname}'
    await db.commit()
    return {'ok':True,'image_url': l.image_url}
