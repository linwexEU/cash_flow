from typing import Annotated

from fastapi import Depends

from src.api.services.category import CategoryService
from src.utils.unit_of_work import SqlAlchemyUnitOfWork


async def get_category_service() -> CategoryService: 
    return CategoryService(SqlAlchemyUnitOfWork())


CategoryServiceDep = Annotated[CategoryService, Depends(get_category_service)]
