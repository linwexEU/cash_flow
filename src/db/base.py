from sqlalchemy.orm import sessionmaker, DeclarativeBase 
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import event

from src.config import settings

engine = create_async_engine(settings.DB_URL)
async_session_factory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False, autoflush=False) 


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record) -> None: 
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class Base(DeclarativeBase): 
    pass
