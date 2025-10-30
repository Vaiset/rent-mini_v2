from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.core.db import Base

class Complaint(Base):
    __tablename__ = 'complaints'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    listing_id: Mapped[int] = mapped_column(ForeignKey('listings.id'))
    from_user_id: Mapped[int | None] = mapped_column(ForeignKey('users.id'), nullable=True)
    text: Mapped[str] = mapped_column(Text)
    contact: Mapped[str | None] = mapped_column(String(120), nullable=True)
    status: Mapped[str] = mapped_column(String(20), default='open')  # open|closed
