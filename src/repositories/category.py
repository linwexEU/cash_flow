from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.models.models import Category 
from src.utils.repository import SqlAlchemyRepository 


class CategoryRepository(SqlAlchemyRepository): 
    _model = Category

    async def select_category_with_subcategories(self) -> Sequence[Category]: 
        query = select(self._model).options(
            selectinload(self._model.subcategory), 
            selectinload(self._model.type_)
        )
        res = await self._session.execute(query) 
        return res.scalars().all() 
