from src.schemas.cash_type import CreateTypeRequest, ViewTypeResponse, CreateTypeResponse, UpdateTypeRequest, \
                                  UpdateTypeResponse, DeleteTypeResponse
from src.utils.service import BaseService
from src.models.enums import ResponseStatus
from src.exceptions.repository import RepositoryIntegrityError, NotFoundError
from src.exceptions.service import CashTypeUniqueError, CashTypeNotFound
from src.utils.logger import log


class CashTypeService(BaseService):
    @log
    async def view_type(self) -> ViewTypeResponse: 
        async with self.uow: 
            res = await self.uow.cash_type_repo.select() 
            return ViewTypeResponse.from_orm(res)

    @log
    async def create_type(self, cash_type: CreateTypeRequest) -> CreateTypeResponse:
        try: 
            async with self.uow: 
                await self.uow.cash_type_repo.create(**cash_type.model_dump()) 
                return CreateTypeResponse(status=ResponseStatus.Success)
        except RepositoryIntegrityError: 
            raise CashTypeUniqueError(f"CashType with name={cash_type.type_name} already exists.")
    
    @log
    async def update_type(self, cash_type_id: int, cash_type: UpdateTypeRequest) -> UpdateTypeResponse: 
        try:
            async with self.uow: 
                await self.uow.cash_type_repo.update_by_id(cash_type_id, **cash_type.model_dump(exclude_none=True))
                return UpdateTypeResponse(status=ResponseStatus.Success)
        except NotFoundError: 
            raise CashTypeNotFound(f"CashType with id={cash_type_id} not found.")

    @log
    async def delete_type(self, cash_type_id: int) -> DeleteTypeResponse: 
        try:
            async with self.uow: 
                await self.uow.cash_type_repo.delete_by_id(cash_type_id)
                return DeleteTypeResponse(status=ResponseStatus.Success)
        except NotFoundError: 
            raise CashTypeNotFound(f"CashType with id={cash_type_id} not found.")
