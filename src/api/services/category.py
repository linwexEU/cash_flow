from src.api.services.commands.cash_type import ValidateCashTypeCommand
from src.api.services.commands.category import ValidateCategoryCommand
from src.models.enums import ResponseStatus
from src.schemas.category import CreateCategoryRequests, CreateCategoryResponse, ViewCategoryResponse, UpdateCategoryRequest, \
                                 UpdateCategoryResponse, DeleteCategoryResponse
from src.utils.service import BaseService
from src.exceptions.repository import RepositoryIntegrityError, NotFoundError
from src.exceptions.service import CashTypeNotFound, TypeDoesNotExist, CategoryNotFound, CategoryUniqueError
from src.utils.logger import log


class CategoryService(BaseService): 
    @log
    async def view_category(self) -> ViewCategoryResponse: 
        async with self.uow: 
            res = await self.uow.category_repo.select_category_with_subcategories()
            return ViewCategoryResponse.from_orm(res)

    @log
    async def create_category(self, category: CreateCategoryRequests) -> CreateCategoryResponse:
        try: 
            async with self.uow: 
                await self.uow.category_repo.create(**category.model_dump())
                return CreateCategoryResponse(status=ResponseStatus.Success) 
        except RepositoryIntegrityError as exc: 
            if "UNIQUE constraint" in str(exc):
                raise CategoryUniqueError(f"Category with name={category.category_name} already exists.")
            raise TypeDoesNotExist(f"CashType with id={category.cash_type} does not exist.") 

    @log
    async def update_category(self, category_id: int, category: UpdateCategoryRequest) -> UpdateCategoryResponse: 
        try:
            async with self.uow: 
                if category.cash_type: 
                    cmd = ValidateCashTypeCommand(self.uow.cash_type_repo, category.cash_type)
                    await cmd.execute()

                cmd = ValidateCategoryCommand(self.uow.category_repo, category_id)
                await cmd.execute() 

                await self.uow.category_repo.update_by_id(category_id, **category.model_dump(exclude_none=True))

                return UpdateCategoryResponse(status=ResponseStatus.Success) 
        except RepositoryIntegrityError:
            raise CategoryUniqueError(f"Category with name={category.category_name} already exists.")
        except CashTypeNotFound: 
            raise
        except CategoryNotFound: 
            raise

    @log
    async def delete_category(self, category_id: int) -> DeleteCategoryResponse:
        try:
            async with self.uow: 
                await self.uow.category_repo.delete_by_id(category_id) 
                return DeleteCategoryResponse(status=ResponseStatus.Success)
        except NotFoundError: 
            raise CategoryNotFound(f"Category with id={category_id} not found.")
