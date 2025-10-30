from src.models.models import SubCategory 
from src.utils.repository import SqlAlchemyRepository 


class SubCategoryRepository(SqlAlchemyRepository): 
    _model = SubCategory
