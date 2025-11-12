from sqlalchemy.orm import sessionmaker, DeclarativeBase 
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import event, NullPool

from src.config import settings


if settings.MODE == "TEST": 
    DATABASE_URL = settings.TEST_DB_URL 
    DATABASE_PARAMS = {"poolclass": NullPool}
else: 
    DATABASE_URL = settings.DB_URL 
    DATABASE_PARAMS = {}


engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)
async_session_factory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False, autoflush=False) 


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record) -> None: 
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class Base(DeclarativeBase): 
    pass
