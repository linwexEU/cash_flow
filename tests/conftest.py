import asyncio
from collections.abc import AsyncGenerator
import json
from pathlib import Path
from typing import Generator, Any

from httpx import AsyncClient, ASGITransport
import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

from src.main import app
from src.db.base import engine, Base, async_session_factory
from src.models.models import CashType, CashStatus, Category, SubCategory
from src.config import settings
from src.utils.unit_of_work import SqlAlchemyUnitOfWork
from tests.fixtures.utils import FakeUnitOfWork


@pytest.fixture(autouse=True, scope="session")
async def prepare_database() -> None: 
    """Fill test database with default data"""
    assert settings.MODE == "TEST"

    async with engine.begin() as conn: 
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str) -> list[dict[str, Any]]: 
        file_path = Path(__file__).parent / f"fixtures/db_mocks/{model}.json"
        with open(file_path, encoding="utf-8") as file: 
            return json.load(file)

    cash_statuses = open_mock_json("cash_status")
    cash_types = open_mock_json("cash_type")
    categories = open_mock_json("category")
    subcategories = open_mock_json("subcategory")

    async with async_session_factory() as session: 
        for status in cash_statuses: 
            query = insert(CashStatus).values(**status)
            await session.execute(query)
        
        for type_ in cash_types: 
            query = insert(CashType).values(**type_)
            await session.execute(query) 
        
        for category in categories: 
            query = insert(Category).values(**category) 
            await session.execute(query)

        for subcategory in subcategories: 
            query = insert(SubCategory).values(**subcategory) 
            await session.execute(query)

        await session.commit()


@pytest_asyncio.fixture(scope="session")
async def session() -> AsyncGenerator[AsyncSession]: 
    async with async_session_factory() as session: 
        yield session


@pytest_asyncio.fixture 
def fake_uow(session: AsyncSession) -> Generator[FakeUnitOfWork]: 
    _fake_uow = FakeUnitOfWork(session) 
    yield _fake_uow


@pytest_asyncio.fixture
async def async_client(fake_uow: FakeUnitOfWork) -> AsyncGenerator:
    app.dependency_overrides[SqlAlchemyUnitOfWork] = lambda: fake_uow 
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac: 
        yield ac
    app.dependency_overrides.clear()


@pytest.fixture(scope="session")
def event_loop(request: pytest.FixtureRequest) -> Generator[asyncio.AbstractEventLoop]: 
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop() 
    yield loop 
    loop.close()
