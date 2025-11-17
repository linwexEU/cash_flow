from src.exceptions.service import IncorrectTypeError
from src.schemas.category import CategoryFilters
from src.api.services.commands.base import Command 
from src.repositories.category import CategoryRepository


class CheckCompatabilityCommand(Command): 
    def __init__(self, category_repo: CategoryRepository, category_id: int, cash_type_id: int) -> None: 
        self.category_repo = category_repo 
        self.category_id = category_id
        self.cash_type_id = cash_type_id

    async def execute(self) -> None: 
        filters = CategoryFilters(id=self.category_id).model_dump(exclude_none=True)
        category = await self.category_repo.select_by_filter_one_or_none(**filters)
        if category.cash_type != self.cash_type_id: 
            raise IncorrectTypeError(f"Category with id={self.category_id} not belong to CashType with id={self.cash_type_id}.")
