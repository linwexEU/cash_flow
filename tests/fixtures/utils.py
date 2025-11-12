from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.cash_flow import CashFlowRepository
from src.repositories.cash_status import CashStatusRepository
from src.repositories.cash_type import CashTypeRepository
from src.repositories.category import CategoryRepository
from src.repositories.subcategory import SubCategoryRepository
from src.utils.unit_of_work import SqlAlchemyUnitOfWork


class FakeUnitOfWork(SqlAlchemyUnitOfWork): 
    def __init__(self, session: AsyncSession) -> None: 
        super().__init__() 
        self._session = session

    async def __aenter__(self) -> None: 
        self.cash_flow_repo = CashFlowRepository(self._session) 
        self.cash_status_repo = CashStatusRepository(self._session) 
        self.cash_type_repo = CashTypeRepository(self._session) 
        self.category_repo = CategoryRepository(self._session) 
        self.subcategory_repo = SubCategoryRepository(self._session)

    async def __aexit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: 
        await self._session.flush() 


class FakeBaseService: 
    def __init__(self, session: AsyncSession) -> None: 
        self.uow = FakeUnitOfWork(session)
