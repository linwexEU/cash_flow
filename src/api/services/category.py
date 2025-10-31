from typing import Annotated

from fastapi import Depends

from src.models.enums import ResponseStatus
from src.schemas.category import CreateCategoryRequests, CreateCategoryResponse, ViewCategoryResponse, UpdateCategoryRequest, \
                                 UpdateCategoryResponse, DeleteCategoryResponse
from src.utils.service import BaseService
from src.utils.unit_of_work import SqlAlchemyUnitOfWork


class CategoryService(BaseService): 
    async def view_category(self) -> ViewCategoryResponse: 
        async with self.uow: 
            res = await self.uow.category_repo.select_category_with_subcategories()
        return ViewCategoryResponse.from_orm(res)

    async def create_category(self, category: CreateCategoryRequests) -> CreateCategoryResponse: 
        async with self.uow: 
            await self.uow.category_repo.create(**category.model_dump())
        return CreateCategoryResponse(Status=ResponseStatus.Success) 

    async def update_category(self, category_id: int, category: UpdateCategoryRequest) -> UpdateCategoryResponse: 
        async with self.uow: 
            await self.uow.category_repo.update_by_id(category_id, **category.model_dump(exclude_none=True))
        return UpdateCategoryResponse(Status=ResponseStatus.Success) 

    async def delete_category(self, category_id: int) -> DeleteCategoryResponse:
        async with self.uow: 
            await self.uow.category_repo.delete_by_id(category_id) 
        return DeleteCategoryResponse(Status=ResponseStatus.Success)


async def get_category_service() -> CategoryService: 
    return CategoryService(SqlAlchemyUnitOfWork())


CategoryServiceDep = Annotated[CategoryService, Depends(get_category_service)]
