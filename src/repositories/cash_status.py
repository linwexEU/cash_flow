from src.models.models import CashStatus 
from src.utils.repository import SqlAlchemyRepository 


class CashStatusRepository(SqlAlchemyRepository): 
    _model = CashStatus
