from collections.abc import Sequence

from pydantic import BaseModel

from src.schemas.base import BaseResponse
from src.models.models import CashType


class TypeInfo(BaseModel): 
    type_id: int
    type_name: str

    @staticmethod
    def from_orm(type_: CashType) -> "TypeInfo": 
        return TypeInfo(type_id=type_.id, type_name=type_.type_name)


class ViewTypeResponse(BaseModel): 
    data: list[TypeInfo]

    @staticmethod 
    def from_orm(cash_type: Sequence[CashType]) -> "ViewTypeResponse": 
        return ViewTypeResponse(data=[TypeInfo(type_id=item.id, type_name=item.type_name) for item in cash_type])


class CreateTypeRequest(BaseModel): 
    type_name: str 


class CreateTypeResponse(BaseResponse): 
    pass 


class UpdateTypeRequest(BaseModel): 
    type_name: str | None = None


class UpdateTypeResponse(BaseResponse): 
    pass


class DeleteTypeResponse(BaseResponse): 
    pass 
