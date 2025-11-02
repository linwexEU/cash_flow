from src.models.enums import ResponseStatus
from src.schemas.cash_status import CreateStatusRequest, CreateStatusResponse, UpdateStatusRequest, \
                                    UpdateStatusResponse, DeleteStatusResponse, ViewStatusResponse
from src.utils.service import BaseService 
from src.exceptions.repository import RepositoryIntegrityError, NotFoundError
from src.exceptions.service import CashStatusNotFound, CashStatusUniqueError
from src.utils.logger import log


class CashStatusService(BaseService):
    @log 
    async def view_status(self) -> ViewStatusResponse: 
        async with self.uow: 
            res = await self.uow.cash_status_repo.select() 
            return ViewStatusResponse.from_orm(res)

    @log
    async def create_status(self, status: CreateStatusRequest) -> CreateStatusResponse: 
        try:
            async with self.uow:
                await self.uow.cash_status_repo.create(**status.model_dump()) 
                return CreateStatusResponse(status=ResponseStatus.Success)
        except RepositoryIntegrityError: 
            raise CashStatusUniqueError(f"CashStatus with name={status.status_name} already exists.")

    @log
    async def update_status(self, status_id: int, status: UpdateStatusRequest) -> UpdateStatusResponse:
        try:
            async with self.uow: 
                await self.uow.cash_status_repo.update_by_id(status_id, **status.model_dump(exclude_none=True))
                return UpdateStatusResponse(status=ResponseStatus.Success)
        except NotFoundError: 
            raise CashStatusNotFound(f"CashStatus with id={status_id} not found.")

    @log
    async def delete_status(self, status_id: int) -> DeleteStatusResponse: 
        try:
            async with self.uow:
                await self.uow.cash_status_repo.delete_by_id(status_id)
                return DeleteStatusResponse(status=ResponseStatus.Success)
        except NotFoundError: 
            raise CashStatusNotFound(f"CashStatus with id={status_id} not found.")
