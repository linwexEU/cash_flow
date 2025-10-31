from typing import Annotated

from fastapi import Depends

from src.schemas.cash_type import CreateTypeRequest, ViewTypeResponse, CreateTypeResponse, UpdateTypeRequest, \
                                  UpdateTypeResponse, DeleteTypeResponse
from src.utils.service import BaseService 
from src.utils.unit_of_work import SqlAlchemyUnitOfWork
from src.models.enums import ResponseStatus


class CashTypeService(BaseService):
    async def view_type(self) -> ViewTypeResponse: 
        async with self.uow: 
            res = await self.uow.cash_type_repo.select() 
        return ViewTypeResponse.from_orm(res)

    async def create_type(self, cash_type: CreateTypeRequest) -> CreateTypeResponse: 
        async with self.uow: 
            await self.uow.cash_type_repo.create(**cash_type.model_dump()) 
        return CreateTypeResponse(Status=ResponseStatus.Success)
    
    async def update_type(self, cash_type_id: int, cash_type: UpdateTypeRequest) -> UpdateTypeResponse: 
        async with self.uow: 
            await self.uow.cash_type_repo.update_by_id(cash_type_id, **cash_type.model_dump(exclude_none=True))
        return UpdateTypeResponse(Status=ResponseStatus.Success)

    async def delete_type(self, cash_type_id: int) -> DeleteTypeResponse: 
        async with self.uow: 
            await self.uow.cash_type_repo.delete_by_id(cash_type_id)
        return DeleteTypeResponse(Status=ResponseStatus.Success)


async def get_cash_type_service() -> CashTypeService: 
    return CashTypeService(SqlAlchemyUnitOfWork())


CashTypeServiceDep = Annotated[CashTypeService, Depends(get_cash_type_service)]
