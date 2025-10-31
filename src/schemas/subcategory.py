from collections.abc import Sequence

from pydantic import BaseModel

from src.models.models import SubCategory
from src.schemas.base import BaseResponse


class SubCategoryInfo(BaseModel): 
    subcategory_id: int
    subcategory_name: str

    @staticmethod
    def from_orm(subcategory: SubCategory) -> "SubCategoryInfo": 
        return SubCategoryInfo(subcategory_id=subcategory.id, subcategory_name=subcategory.subcategory_name)


class CreateSubCategoryRequest(BaseModel): 
    parent_category: int 
    subcategory_name: str


class CreateSubCategoryResponse(BaseResponse): 
    pass 


class ViewSubCategoryResponse(BaseModel):
    data: list[SubCategoryInfo]

    @staticmethod
    def from_orm(subcategory: Sequence[SubCategory]) -> "ViewSubCategoryResponse": 
        return ViewSubCategoryResponse(data=[SubCategoryInfo.from_orm(item) for item in subcategory])


class UpdateSubCategoryRequest(BaseModel): 
    subcategory_name: str | None = None
    parent_category: int | None = None 


class UpdateSubCategoryResponse(BaseResponse): 
    pass 


class DeleteSubCategoryResponse(BaseResponse):
    pass 
