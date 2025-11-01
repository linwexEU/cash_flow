from typing import Annotated

from fastapi import Depends

from src.api.services.cash_status import CashStatusService
from src.utils.unit_of_work import SqlAlchemyUnitOfWork


async def get_cash_status_service() -> CashStatusService: 
    return CashStatusService(SqlAlchemyUnitOfWork())


CashStatusServiceDep = Annotated[CashStatusService, Depends(get_cash_status_service)]
