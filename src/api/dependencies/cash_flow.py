from typing import Annotated

from fastapi import Depends

from src.api.services.cash_flow import CashFlowService
from src.utils.unit_of_work import SqlAlchemyUnitOfWork


async def get_cash_flow_service() -> CashFlowService: 
    return CashFlowService(SqlAlchemyUnitOfWork())


CashFlowServiceDep = Annotated[CashFlowService, Depends(get_cash_flow_service)]
