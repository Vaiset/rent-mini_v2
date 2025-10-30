from sqlalchemy import BigInteger, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.core.db import Base

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    role: Mapped[str] = mapped_column(String(20), default='seeker')  # seeker | realtor | admin
    name: Mapped[str | None] = mapped_column(String(120), nullable=True)
    country: Mapped[str | None] = mapped_column(String(80), nullable=True)
    city: Mapped[str | None] = mapped_column(String(80), nullable=True)
    locale: Mapped[str | None] = mapped_column(String(8), nullable=True)  # en, ru, ro, de, es, fr, ar, he, pl, cs
    contact_telegram: Mapped[str | None] = mapped_column(String(64), nullable=True)  # @username
    active: Mapped[bool] = mapped_column(Boolean, default=True)  # admin can block
