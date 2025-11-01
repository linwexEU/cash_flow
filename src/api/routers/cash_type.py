from fastapi import APIRouter, status

from src.api.dependencies.cash_type import CashTypeServiceDep
from src.schemas.cash_type import CreateTypeRequest, ViewTypeResponse, CreateTypeResponse, UpdateTypeRequest, \
                                  UpdateTypeResponse, DeleteTypeResponse

router = APIRouter()


@router.get("/")
async def view_type(service: CashTypeServiceDep) -> ViewTypeResponse: 
    return await service.view_type()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_type(cash_type: CreateTypeRequest, service: CashTypeServiceDep) -> CreateTypeResponse: 
    return await service.create_type(cash_type)


@router.patch("/{type_id}")
async def update_type(type_id: int, cash_type: UpdateTypeRequest, service: CashTypeServiceDep) -> UpdateTypeResponse: 
    return await service.update_type(type_id, cash_type) 


@router.delete("/{type_id}")
async def delete_type(type_id: int, service: CashTypeServiceDep) -> DeleteTypeResponse: 
    return await service.delete_type(type_id)
