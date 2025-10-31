__all__ = (
    "router",
)

from fastapi import APIRouter

from src.api.routers.cash_status import router as cash_status_router
from src.api.routers.cash_type import router as cash_type_router
from src.api.routers.category import router as category_router
from src.api.routers.subcategory import router as subcategory_router

router = APIRouter()

router.include_router(cash_status_router, prefix="/status", tags=["Cash Status"])
router.include_router(cash_type_router, prefix="/type", tags=["Cash Type"])
router.include_router(category_router, prefix="/category", tags=["Category"])
router.include_router(subcategory_router, prefix="/subcategory", tags=["SubCategory"])
