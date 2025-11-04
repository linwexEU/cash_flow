from src.api.services.commands.cash_flow import ValidateCategoryCommand
from src.api.services.commands.cash_type import ValidateCashTypeCommand
from src.utils.service import BaseService 
from src.schemas.cash_flow import CreateCashFlowRequest, CreateCashFlowResponse, ViewCashFlowResponse, DeleteCashFlowResponse, \
                                  UpdateCashFlowRequest, UpdateCashFlowResponse, CashFlowFilters
from src.models.enums import ResponseStatus
from src.exceptions.service import CashFlowNotFound, CategoryNotFound, IncorrectTypeError, CashTypeNotFound
from src.exceptions.repository import NotFoundError
from src.utils.logger import log


class CashFlowService(BaseService):
    @log 
    async def view_cash_flow(self) -> ViewCashFlowResponse: 
        async with self.uow: 
            res = await self.uow.cash_flow_repo.load_cash_flow()
            return ViewCashFlowResponse.from_orm(res)

    @log
    async def create_cash_flow(self, cash_flow: CreateCashFlowRequest) -> CreateCashFlowResponse:
        try:
            async with self.uow: 
                category_cmd = ValidateCategoryCommand(self.uow.category_repo, cash_flow.category, cash_flow.cash_type)
                cash_type_cmd = ValidateCashTypeCommand(self.uow.cash_type_repo, cash_flow.cash_type)

                await cash_type_cmd.execute() 
                await category_cmd.execute()

                await self.uow.cash_flow_repo.create(**cash_flow.model_dump())

                return CreateCashFlowResponse(status=ResponseStatus.Success)
        except CashTypeNotFound: 
            raise 
        except CategoryNotFound: 
            raise
        except IncorrectTypeError: 
            raise
    
    @log
    async def update_cash_flow(self, cash_flow_id: int, cash_flow: UpdateCashFlowRequest) -> UpdateCashFlowResponse: 
        try:
            async with self.uow: 
                # Get CashFlow 
                filters = CashFlowFilters(id=cash_flow_id)
                cash_flow_db = await self.uow.cash_flow_repo.select_by_filter_one_or_none(**filters.model_dump(exclude_none=True))

                cash_type_id = cash_flow.cash_type if cash_flow.cash_type is not None else cash_flow_db.cash_type
                category_id = cash_flow.category if cash_flow.category is not None else cash_flow_db.category

                category_cmd = ValidateCategoryCommand(self.uow.category_repo, category_id, cash_type_id)
                cash_type_cmd = ValidateCashTypeCommand(self.uow.cash_type_repo, cash_type_id)

                # Validate CashType with Category
                await cash_type_cmd.execute() 
                await category_cmd.execute()

                await self.uow.cash_flow_repo.update_by_id(cash_flow_id, **cash_flow.model_dump(exclude_none=True)) 

                return UpdateCashFlowResponse(status=ResponseStatus.Success)
        except CashTypeNotFound: 
            raise 
        except CategoryNotFound: 
            raise
        except IncorrectTypeError: 
            raise
        except AttributeError: 
            raise CashFlowNotFound(f"CashFlow with id={cash_flow_id} not found.")
        
    @log
    async def delete_cash_flow(self, cash_flow_id: int) -> DeleteCashFlowResponse: 
        try:
            async with self.uow: 
                await self.uow.cash_flow_repo.delete_by_id(cash_flow_id) 
                return DeleteCashFlowResponse(status=ResponseStatus.Success)   
        except NotFoundError: 
            raise CashFlowNotFound(f"CashFlow with id={cash_flow_id} not found.")
