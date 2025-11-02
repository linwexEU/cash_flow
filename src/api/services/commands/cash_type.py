from src.exceptions.service import CashTypeNotFound
from src.schemas.cash_type import CashTypeFilters
from src.api.services.commands.base import Command 
from src.repositories.cash_type import CashTypeRepository


class ValidateCashTypeCommand(Command): 
    def __init__(self, repo: CashTypeRepository, cash_type_id: int) -> None: 
        self.repo = repo 
        self.cash_type_id = cash_type_id

    async def execute(self) -> None: 
        filters = CashTypeFilters(id=self.cash_type_id).model_dump(exclude_none=True)
        cash_type = await self.repo.select_by_filter_one_or_none(**filters)

        if cash_type is None: 
            raise CashTypeNotFound(f"CashType with id={self.cash_type_id} not found.")
