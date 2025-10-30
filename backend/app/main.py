from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.db import init_db
from app.routers import auth, listings, users, realtors, complaints

app = FastAPI(title="RentMini v2 API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event('startup')
async def on_startup():
    await init_db()

@app.get('/api/health')
async def health():
    return {"status": "ok"}

app.include_router(auth.router)
app.include_router(listings.router)
app.include_router(users.router)
app.include_router(realtors.router)
app.include_router(complaints.router)
