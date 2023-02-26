from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BIGINT, DateTime
from sqlalchemy.ext.asyncio import AsyncSession

from .base import Base

from datetime import datetime


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    @staticmethod
    async def create(session: AsyncSession, user_id: int) -> 'User':
        user = User(id=user_id)
        session.add(user)
        return user
    
    @staticmethod
    async def get(session: AsyncSession, user_id: int) -> 'User':
        return await session.get(User, user_id)