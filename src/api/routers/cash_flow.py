from fastapi import APIRouter

from src.schemas.cash_flow import CreateCashFlowRequest, CreateCashFlowResponse, ViewCashFlowResponse, DeleteCashFlowResponse
from src.api.dependencies.cash_flow import CashFlowServiceDep

router = APIRouter()


@router.get("/")
async def view_cash_flow(service: CashFlowServiceDep) -> ViewCashFlowResponse: 
    return await service.view_cash_flow()


@router.post("/")
async def create_cash_flow(cash_flow: CreateCashFlowRequest, service: CashFlowServiceDep) -> CreateCashFlowResponse: 
    return await service.create_cash_flow(cash_flow)


@router.delete("/{cash_flow_id}")
async def delete_cash_flow(cash_flow_id: int, service: CashFlowServiceDep) -> DeleteCashFlowResponse: 
    return await service.delete_cash_flow(cash_flow_id)
