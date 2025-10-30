from sqlalchemy.orm import sessionmaker, DeclarativeBase 
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from src.config import settings

engine = create_async_engine(settings.DB_URL)
async_session_factory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False, autoflush=False) 


class Base(DeclarativeBase): 
    pass
