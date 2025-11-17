from src.api.services.commands.category import ValidateCategoryCommand
from src.schemas.subcategory import CreateSubCategoryRequest, CreateSubCategoryResponse, ViewSubCategoryResponse, \
                                    UpdateSubCategoryRequest, UpdateSubCategoryResponse, DeleteSubCategoryResponse
from src.utils.service import BaseService
from src.models.enums import ResponseStatus
from src.exceptions.repository import RepositoryIntegrityError, NotFoundError
from src.exceptions.service import CategorDoesNotExist, CategoryNotFound, SubCategoryNotFound, SubCategoryUniqueError
from src.utils.logger import log


class SubCategoryService(BaseService):
    @log
    async def view_subcategory(self) -> ViewSubCategoryResponse: 
        async with self.uow: 
            res = await self.uow.subcategory_repo.select()
            return ViewSubCategoryResponse.from_orm(res)

    @log
    async def create_subcategory(self, subcategory: CreateSubCategoryRequest) -> CreateSubCategoryResponse: 
        try:
            async with self.uow: 
                await self.uow.subcategory_repo.create(**subcategory.model_dump()) 
                return CreateSubCategoryResponse(status=ResponseStatus.Success)
        except RepositoryIntegrityError as exc: 
            if "UNIQUE constraint" in str(exc): 
                raise SubCategoryUniqueError(f"SubCategory with name={subcategory.subcategory_name} already exists.")
            raise CategorDoesNotExist(f"Category with id={subcategory.parent_category} does not exist.")

    @log
    async def update_subcategory(self, subcategory_id: int, subcategory: UpdateSubCategoryRequest) -> UpdateSubCategoryResponse:
        try: 
            async with self.uow:
                if subcategory.parent_category:
                    cmd = ValidateCategoryCommand(self.uow.category_repo, subcategory.parent_category)
                    await cmd.execute() 

                await self.uow.subcategory_repo.update_by_id(subcategory_id, **subcategory.model_dump(exclude_none=True)) 
                return UpdateSubCategoryResponse(status=ResponseStatus.Success) 
        except CategoryNotFound: 
            raise 
        except RepositoryIntegrityError:
            raise SubCategoryUniqueError(f"Subcategory with name={subcategory.subcategory_name} already exists.")
        except NotFoundError: 
            raise SubCategoryNotFound(f"SubCategory with id={subcategory_id} not found.")

    @log
    async def delete_subcategory(self, subcategory_id: int) -> DeleteSubCategoryResponse:
        try: 
            async with self.uow: 
                await self.uow.subcategory_repo.delete_by_id(subcategory_id)
                return DeleteSubCategoryResponse(status=ResponseStatus.Success) 
        except NotFoundError: 
            raise SubCategoryNotFound(f"SubCategory with id={subcategory_id} not found.")
