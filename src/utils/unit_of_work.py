from abc import ABC, abstractmethod 
from typing import Any

from src.db.base import async_session_factory
from src.utils.repository import AbstractRepository
from src.repositories import CashFlowRepository, CashTypeRepository, CashStatusRepository, \
                             CategoryRepository, SubCategoryRepository


class AbstractUnitOfWork(ABC): 
    cash_status_repo: AbstractRepository
    cash_type_repo: AbstractRepository
    cash_flow_repo: AbstractRepository
    category_repo: AbstractRepository
    subcategory_repo: AbstractRepository

    @abstractmethod
    async def commit(self) -> None: ... 

    @abstractmethod
    async def rollback(self) -> None: ...

    @abstractmethod
    async def __aenter__(self) -> "AbstractUnitOfWork": ...

    @abstractmethod
    async def __aexit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...


class SqlAlchemyUnitOfWork(AbstractUnitOfWork): 
    def __init__(self) -> None: 
        self.session = async_session_factory()

    async def commit(self) -> None: 
        await self.session.commit()

    async def rollback(self) -> None: 
        await self.session.rollback()

    async def __aenter__(self) -> "SqlAlchemyUnitOfWork": 
        self.cash_flow_repo = CashFlowRepository(self.session) 
        self.cash_status_repo = CashStatusRepository(self.session) 
        self.cash_type_repo = CashTypeRepository(self.session) 
        self.category_repo = CategoryRepository(self.session) 
        self.subcategory_repo = SubCategoryRepository(self.session)
        return self
    
    async def __aexit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        if exc_type is None:
            await self.commit()
        else: 
            await self.rollback()
        await self.session.close()
