from fastapi import APIRouter, status

from src.api.services.category import CategoryServiceDep
from src.schemas.category import CreateCategoryRequests, CreateCategoryResponse, ViewCategoryResponse, UpdateCategoryRequest, \
                                 UpdateCategoryResponse, DeleteCategoryResponse

router = APIRouter()


@router.get("/")
async def view_category(service: CategoryServiceDep) -> ViewCategoryResponse: 
    return await service.view_category()


@router.post("/", status_code=status.HTTP_201_CREATED) 
async def create_category(category: CreateCategoryRequests, service: CategoryServiceDep) -> CreateCategoryResponse: 
    return await service.create_category(category)


@router.patch("/{category_id}")
async def update_category(category_id: int, category: UpdateCategoryRequest, service: CategoryServiceDep) -> UpdateCategoryResponse: 
    return await service.update_category(category_id, category)


@router.delete("/{category_id}")
async def delete_category(category_id: int, service: CategoryServiceDep) -> DeleteCategoryResponse: 
    return await service.delete_category(category_id)
