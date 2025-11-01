from fastapi import APIRouter, status

from src.api.dependencies.cash_status import CashStatusServiceDep
from src.schemas.cash_status import CreateStatusRequest, CreateStatusResponse, UpdateStatusRequest, UpdateStatusResponse, \
                                    DeleteStatusResponse, ViewStatusResponse


router = APIRouter()


@router.get("/")
async def view_status(service: CashStatusServiceDep) -> ViewStatusResponse: 
    return await service.view_status()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_status(status: CreateStatusRequest, service: CashStatusServiceDep) -> CreateStatusResponse: 
    return await service.create_status(status)


@router.patch("/{status_id}")
async def update_status(status_id: int, status: UpdateStatusRequest, service: CashStatusServiceDep) -> UpdateStatusResponse: 
    return await service.update_status(status_id, status)


@router.delete("/{status_id}")
async def delete_status(status_id: int, service: CashStatusServiceDep) -> DeleteStatusResponse: 
    return await service.delete_status(status_id)
