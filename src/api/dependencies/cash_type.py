from typing import Annotated

from fastapi import Depends

from src.api.services.cash_type import CashTypeService
from src.utils.unit_of_work import SqlAlchemyUnitOfWork


async def get_cash_type_service() -> CashTypeService: 
    return CashTypeService(SqlAlchemyUnitOfWork())


CashTypeServiceDep = Annotated[CashTypeService, Depends(get_cash_type_service)]
