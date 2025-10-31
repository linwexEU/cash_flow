from collections.abc import Sequence

from pydantic import BaseModel

from src.schemas.base import BaseResponse
from src.models.models import CashStatus


class StatusInfo(BaseModel): 
    status_id: int 
    status_name: str 


class ViewStatusResponse(BaseModel): 
    data: list[StatusInfo]

    @staticmethod
    def from_orm(status: Sequence[CashStatus]) -> "ViewStatusResponse": 
        return ViewStatusResponse(data=[StatusInfo(status_id=item.id, status_name=item.status_name) for item in status])


class CreateStatusRequest(BaseModel): 
    status_name: str


class CreateStatusResponse(BaseResponse): 
    pass 


class UpdateStatusRequest(BaseModel): 
    status_name: str | None = None


class UpdateStatusResponse(BaseResponse): 
    pass 


class DeleteStatusResponse(BaseResponse): 
    pass 
