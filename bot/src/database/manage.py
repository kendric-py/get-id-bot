from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL


async_engine = create_async_engine(DATABASE_URL, echo=False, future=True)
async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)
