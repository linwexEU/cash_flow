import asyncio
import json
import os
from pathlib import Path
from typing import Generator, Any

import pytest
from sqlalchemy import insert

from src.db.base import engine, Base, async_session_factory
from src.models.models import CashType, CashStatus, Category, SubCategory
from src.config import settings


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
    

@pytest.fixture(scope="session")
def event_loop(request: pytest.FixtureRequest) -> Generator[asyncio.AbstractEventLoop]: 
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop() 
    yield loop 
    loop.close()
