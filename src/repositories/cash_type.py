from src.models.models import CashType 
from src.utils.repository import SqlAlchemyRepository 


class CashTypeRepository(SqlAlchemyRepository): 
    _model = CashType
