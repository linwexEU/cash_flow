from typing import Annotated

from fastapi import Depends

from src.models.enums import ResponseStatus
from src.schemas.cash_status import CreateStatusRequest, CreateStatusResponse, UpdateStatusRequest, \
                                    UpdateStatusResponse, DeleteStatusResponse, ViewStatusResponse
from src.utils.service import BaseService 
from src.utils.unit_of_work import SqlAlchemyUnitOfWork


class CashStatusService(BaseService): 
    async def view_status(self) -> ViewStatusResponse: 
        async with self.uow: 
            res = await self.uow.cash_status_repo.select() 
        return ViewStatusResponse.from_orm(res)

    async def create_status(self, status: CreateStatusRequest) -> CreateStatusResponse: 
        async with self.uow:
            await self.uow.cash_status_repo.create(**status.model_dump()) 
        return CreateStatusResponse(Status=ResponseStatus.Success)

    async def update_status(self, status_id: int, status: UpdateStatusRequest) -> UpdateStatusResponse:
        async with self.uow: 
            await self.uow.cash_status_repo.update_by_id(status_id, **status.model_dump(exclude_none=True))
        return UpdateStatusResponse(Status=ResponseStatus.Success)

    async def delete_status(self, status_id: int) -> DeleteStatusResponse: 
        async with self.uow:
            await self.uow.cash_status_repo.delete_by_id(status_id)
        return DeleteStatusResponse(Status=ResponseStatus.Success)


async def get_cash_status_service() -> CashStatusService: 
    return CashStatusService(SqlAlchemyUnitOfWork())


CashStatusServiceDep = Annotated[CashStatusService, Depends(get_cash_status_service)]
