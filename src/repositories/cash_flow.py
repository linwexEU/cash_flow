from src.models.models import CashFlow
from src.utils.repository import SqlAlchemyRepository 


class CashFlowRepository(SqlAlchemyRepository): 
    _model = CashFlow
