from collections.abc import Sequence

from pydantic import BaseModel

from src.schemas.base import BaseResponse
from src.models.models import CashStatus


class StatusInfo(BaseModel): 
    status_id: int 
    status_name: str 

    @staticmethod
    def from_orm(status: CashStatus) -> "StatusInfo": 
        return StatusInfo(
            status_id=status.id, 
            status_name=status.status_name
        )


class ViewStatusResponse(BaseModel): 
    data: list[StatusInfo]

    @staticmethod
    def from_orm(status: Sequence[CashStatus]) -> "ViewStatusResponse": 
        return ViewStatusResponse(data=[StatusInfo.from_orm(item) for item in status])


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
