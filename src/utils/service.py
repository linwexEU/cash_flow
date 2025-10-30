from fastapi import Depends

from src.utils.unit_of_work import SqlAlchemyUnitOfWork
from src.utils.repository import AbstractRepository


class BaseService: 
    _repo: str 

    def __init__(self, uow: SqlAlchemyUnitOfWork = Depends()) -> None: 
        self.uow: SqlAlchemyUnitOfWork = uow

        if not hasattr(self, "_repo"): 
            err_msg = f"Attribute '_repo' is required for class {self.__class__.__name__}"
            raise AttributeError(err_msg)

    def _get_related_repo(self) -> AbstractRepository: 
        return getattr(self.uow, self._repo)
