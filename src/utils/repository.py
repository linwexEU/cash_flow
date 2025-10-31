from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Any, Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession 
from sqlalchemy import select, insert, update, delete

from src.db.base import Base

M = TypeVar("M", bound=Base)


class AbstractRepository(ABC): 
    @abstractmethod
    def __init__(self, session: AsyncSession) -> None: ...

    @abstractmethod
    async def create(self, *args: Any, **kwargs: Any) -> None: ... 

    @abstractmethod
    async def select(self, *args: Any, **kwargs: Any) -> Sequence[M]: ...

    @abstractmethod
    async def select_by_filter_all(self, *args: Any, **kwargs: Any) -> Sequence[M]: ...

    @abstractmethod 
    async def select_by_filter_one_or_none(self, *args: Any, **kwargs: Any) -> M | None: ... 

    @abstractmethod
    async def update_by_id(self, *args: Any, **kwargs: Any) -> None: ... 
    
    @abstractmethod
    async def delete_by_id(self, *args: Any, **kwargs: Any) -> None: ...


class SqlAlchemyRepository(AbstractRepository):     
    _model: type[M]

    def __init__(self, session: AsyncSession) -> None: 
        self._session = session

    async def create(self, **kwargs: Any) -> None: 
        query = insert(self._model).values(**kwargs) 
        await self._session.execute(query)

    async def select(self) -> Sequence[M]:
        query = select(self._model)
        res = await self._session.execute(query) 
        return res.scalars().all()

    async def select_by_filter_all(self, **kwargs: Any) -> Sequence[M]: 
        query = select(self._model).filter_by(**kwargs)
        res = await self._session.execute(query)
        return res.scalars().all()
    
    async def select_by_filter_one_or_none(self, **kwargs: Any) -> M | None: 
        query = select(self._model).filter_by(**kwargs)
        res = await self._session.execute(query) 
        return res.scalar_one_or_none()
    
    async def update_by_id(self, obj_id: int, **kwargs: Any) -> None: 
        query = update(self._model).values(**kwargs).where(self._model.id == obj_id)
        await self._session.execute(query) 

    async def delete_by_id(self, obj_id: int) -> None: 
        query = delete(self._model).where(self._model.id == obj_id)
        await self._session.execute(query)
