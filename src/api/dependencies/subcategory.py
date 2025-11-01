from typing import Annotated

from fastapi import Depends

from src.api.services.subcategory import SubCategoryService
from src.utils.unit_of_work import SqlAlchemyUnitOfWork


async def get_subcategory_service() -> SubCategoryService: 
    return SubCategoryService(SqlAlchemyUnitOfWork())


SubCategoryServiceDep = Annotated[SubCategoryService, Depends(get_subcategory_service)]
