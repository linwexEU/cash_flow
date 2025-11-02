from collections.abc import Sequence

from pydantic import BaseModel

from src.schemas.cash_type import TypeInfo
from src.schemas.base import BaseResponse
from src.models.models import Category
from src.schemas.subcategory import SubCategoryInfo


class CategoryInfo(BaseModel): 
    caterogy_id: int 
    category_name: str
    cash_type: TypeInfo
    subcategories: list[SubCategoryInfo]

    @staticmethod
    def from_orm(category: Category) -> "CategoryInfo":
        subcategories = [SubCategoryInfo.from_orm(item) for item in category.subcategory]
        return CategoryInfo(
            caterogy_id=category.id, 
            category_name=category.category_name, 
            cash_type=TypeInfo.from_orm(category.type_),
            subcategories=subcategories
        )


class ShortCategoryInfo(BaseModel): 
    caterogy_id: int 
    category_name: str
    subcategories: list[SubCategoryInfo]

    @staticmethod
    def from_orm(category: Category) -> "ShortCategoryInfo":
        subcategories = [SubCategoryInfo.from_orm(item) for item in category.subcategory]
        return ShortCategoryInfo(
            caterogy_id=category.id, 
            category_name=category.category_name,
            subcategories=subcategories
        )


class ViewCategoryResponse(BaseModel): 
    data: list[CategoryInfo] 

    @staticmethod
    def from_orm(categories: Sequence[Category]) -> "ViewCategoryResponse":
        return ViewCategoryResponse(data=[CategoryInfo.from_orm(category) for category in categories])


class CreateCategoryRequests(BaseModel):
    cash_type: int 
    category_name: str


class CreateCategoryResponse(BaseResponse): 
    pass 


class UpdateCategoryRequest(BaseModel): 
    category_name: str | None = None
    cash_type: int | None = None


class UpdateCategoryResponse(BaseResponse):
    pass 


class DeleteCategoryResponse(BaseResponse): 
    pass 


class CategoryFilters(BaseModel):
    id: int | None = None 
    category_name: str | None = None
    cash_type: int | None = None
