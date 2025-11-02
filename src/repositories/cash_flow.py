from collections.abc import Sequence

from sqlalchemy.orm import selectinload
from sqlalchemy import select

from src.models.models import CashFlow, Category
from src.utils.repository import SqlAlchemyRepository 


class CashFlowRepository(SqlAlchemyRepository): 
    _model = CashFlow

    async def load_cash_flow(self) -> Sequence[CashFlow]: 
        query = select(self._model).options(
            selectinload(self._model.cash_status_rel), 
            selectinload(self._model.cash_type_rel),
            selectinload(self._model.category_rel).selectinload(Category.subcategory) 
        )
        res = await self._session.execute(query) 
        return res.scalars().all()
