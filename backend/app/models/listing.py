from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.db import Base

class Listing(Base):
    __tablename__ = 'listings'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200))
    price: Mapped[int] = mapped_column(Integer)
    realtor_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    realtor = relationship('User')
