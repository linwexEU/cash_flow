from fastapi import APIRouter, status

from src.schemas.cash_flow import CashFlowSpecifications, CreateCashFlowRequest, CreateCashFlowResponse, ViewCashFlowResponse, DeleteCashFlowResponse, \
                                  UpdateCashFlowRequest, UpdateCashFlowResponse
from src.api.dependencies.cash_flow import CashFlowServiceDep

router = APIRouter()


@router.get("/")
async def view_cash_flow(service: CashFlowServiceDep) -> ViewCashFlowResponse: 
    return await service.view_cash_flow()


@router.post("/specifications")
async def view_cash_flow_specifications(specifications: CashFlowSpecifications, service: CashFlowServiceDep) -> ViewCashFlowResponse: 
    return await service.view_cash_flow_with_spec(specifications) 


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_cash_flow(cash_flow: CreateCashFlowRequest, service: CashFlowServiceDep) -> CreateCashFlowResponse: 
    return await service.create_cash_flow(cash_flow)


@router.patch("/{cash_flow_id}")
async def udpate_cash_flow(cash_flow_id: int, cash_flow: UpdateCashFlowRequest, service: CashFlowServiceDep) -> UpdateCashFlowResponse: 
    return await service.update_cash_flow(cash_flow_id, cash_flow)


@router.delete("/{cash_flow_id}")
async def delete_cash_flow(cash_flow_id: int, service: CashFlowServiceDep) -> DeleteCashFlowResponse: 
    return await service.delete_cash_flow(cash_flow_id)
