from typing import Annotated

from fastapi import Depends 

from src.schemas.subcategory import CreateSubCategoryRequest, CreateSubCategoryResponse, ViewSubCategoryResponse, \
                                    UpdateSubCategoryRequest, UpdateSubCategoryResponse, DeleteSubCategoryResponse
from src.utils.service import BaseService
from src.models.enums import ResponseStatus
from src.utils.unit_of_work import SqlAlchemyUnitOfWork


class SubCategoryService(BaseService):
    async def view_subcategory(self) -> ViewSubCategoryResponse: 
        async with self.uow: 
            res = await self.uow.subcategory_repo.select() 
        return ViewSubCategoryResponse.from_orm(res) 

    async def create_subcategory(self, subcategory: CreateSubCategoryRequest) -> CreateSubCategoryResponse: 
        async with self.uow: 
            await self.uow.subcategory_repo.create(**subcategory.model_dump()) 
        return CreateSubCategoryResponse(Status=ResponseStatus.Success)

    async def update_subcategory(self, subcategory_id: int, subcategory: UpdateSubCategoryRequest) -> UpdateSubCategoryResponse: 
        async with self.uow: 
            await self.uow.subcategory_repo.update_by_id(subcategory_id, **subcategory.model_dump(exclude_none=True)) 
        return UpdateSubCategoryResponse(Status=ResponseStatus.Success) 

    async def delete_subcategory(self, subcategory_id: int) -> DeleteSubCategoryResponse: 
        async with self.uow: 
            await self.uow.subcategory_repo.delete_by_id(subcategory_id)
        return DeleteSubCategoryResponse(Status=ResponseStatus.Success) 


async def get_subcategory_service() -> SubCategoryService: 
    return SubCategoryService(SqlAlchemyUnitOfWork())


SubCategoryServiceDep = Annotated[SubCategoryService, Depends(get_subcategory_service)]
