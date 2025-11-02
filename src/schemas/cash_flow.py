from collections.abc import Sequence

from pydantic import BaseModel

from src.schemas.cash_type import TypeInfo
from src.models.models import CashFlow
from src.schemas.base import BaseResponse
from src.schemas.cash_status import StatusInfo
from src.schemas.category import ShortCategoryInfo


class CreateCashFlowRequest(BaseModel): 
    cash_status: int
    cash_type: int
    category: int
    amount: float
    comment: str | None = None


class CreateCashFlowResponse(BaseResponse): 
    pass 


class CashFlowInfo(BaseModel):
    create_utc: str 
    cash_flow_id: int
    cash_status: StatusInfo
    cash_type: TypeInfo
    category: ShortCategoryInfo
    amount: float
    comment: str | None = None

    @staticmethod
    def from_orm(cash_flow: CashFlow) -> "CashFlowInfo": 
        return CashFlowInfo(
            create_utc=cash_flow.create_utc.strftime('%d.%m.%Y'),
            cash_flow_id=cash_flow.id, 
            cash_status=StatusInfo.from_orm(cash_flow.cash_status_rel), 
            cash_type=TypeInfo.from_orm(cash_flow.cash_type_rel),
            category=ShortCategoryInfo.from_orm(cash_flow.category_rel), 
            amount=cash_flow.amount, 
            comment=cash_flow.comment
        )


class ViewCashFlowResponse(BaseModel): 
    data: list[CashFlowInfo]

    @staticmethod
    def from_orm(cash_flows: Sequence[CashFlow]) -> "ViewCashFlowResponse": 
        return ViewCashFlowResponse(data=[CashFlowInfo.from_orm(cash_flow) for cash_flow in cash_flows])


class DeleteCashFlowResponse(BaseResponse): 
    pass 
