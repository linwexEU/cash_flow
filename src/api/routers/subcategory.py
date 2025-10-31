from fastapi import APIRouter, status

from src.api.services.subcategory import SubCategoryServiceDep
from src.schemas.subcategory import CreateSubCategoryRequest, CreateSubCategoryResponse, ViewSubCategoryResponse, \
                                    UpdateSubCategoryRequest, UpdateSubCategoryResponse, DeleteSubCategoryResponse
from src.api.services.subcategory import SubCategoryServiceDep

router = APIRouter() 


@router.get("/")
async def view_subcategory(service: SubCategoryServiceDep) -> ViewSubCategoryResponse: 
    return await service.view_subcategory()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_subcategory(subcategory: CreateSubCategoryRequest, service: SubCategoryServiceDep) -> CreateSubCategoryResponse: 
    return await service.create_subcategory(subcategory)


@router.patch("/{subcategory_id}")
async def update_subcategory(subcategory_id: int , subcategory: UpdateSubCategoryRequest, service: SubCategoryServiceDep) -> UpdateSubCategoryResponse: 
    return await service.update_subcategory(subcategory_id, subcategory)


@router.delete("/{subcategory_id}")
async def delete_subcategory(subcategory_id: int, service: SubCategoryServiceDep) -> DeleteSubCategoryResponse: 
    return await service.delete_subcategory(subcategory_id)
