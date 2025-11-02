from src.exceptions.service import CategoryNotFound, IncorrectTypeError
from src.schemas.category import CategoryFilters
from src.api.services.commands.base import Command
from src.repositories.category import CategoryRepository


class ValidateCategoryCommand(Command): 
    def __init__(self, repo: CategoryRepository, category_id: int, cash_type_id: int) -> None: 
        self.repo = repo
        self.category_id = category_id 
        self.cash_type_id = cash_type_id

    async def execute(self) -> None:
        filters = CategoryFilters(id=self.category_id).model_dump(exclude_none=True)
        category = await self.repo.select_by_filter_one_or_none(**filters)

        if category is None: 
            raise CategoryNotFound(f"Category with id={self.category_id} not found.")

        if category.cash_type != self.cash_type_id: 
            raise IncorrectTypeError(f"Category with id={self.category_id} does not belong to CashType with id={self.cash_type_id}.")
