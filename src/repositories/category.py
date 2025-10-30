from src.models.models import Category 
from src.utils.repository import SqlAlchemyRepository 


class CategoryRepository(SqlAlchemyRepository): 
    _model = Category
