from collections.abc import Sequence

from sqlalchemy.orm import selectinload
from sqlalchemy import select

from src.models.models import CashFlow, Category, SubCategory, CashStatus, CashType
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

    async def select_with_specifications(self, specifications: dict) -> Sequence[CashFlow]: 
        query = select(self._model).options(
            selectinload(self._model.cash_status_rel), 
            selectinload(self._model.cash_type_rel), 
            selectinload(self._model.category_rel).selectinload(Category.subcategory)
        )

        if start_utc := specifications.get("start_utc"): 
            query = query.where(self._model.create_utc >= start_utc)

        if end_utc := specifications.get("end_utc"):
            query = query.where(self._model.create_utc <= end_utc)

        if cash_status := specifications.get("cash_status"): 
            query = query.where(CashStatus.id == cash_status)

        if cash_type := specifications.get("cash_type"): 
            query = query.where(CashType.id == cash_type)

        if category := specifications.get("category"): 
            query = query.where(Category.id == category)

        if specifications.get("subcategory"): 
            query = query.where(
                CashFlow.category_rel.has(Category.subcategory.any(SubCategory.id == 3))
            )

        res = await self._session.execute(query) 
        return res.scalars().all()
