

class ServiceError(Exception): 
    pass 


class CategorDoesNotExist(ServiceError): 
    pass 


class CategoryUniqueError(ServiceError): 
    pass 


class SubCategoryUniqueError(ServiceError): 
    pass 


class CashTypeUniqueError(ServiceError):
    pass 


class CashTypeNotFound(ServiceError): 
    pass 


class CashStatusNotFound(ServiceError): 
    pass 


class CashStatusUniqueError(ServiceError): 
    pass 


class TypeDoesNotExist(ServiceError): 
    pass 


class SubCategoryNotFound(ServiceError): 
    pass 


class CategoryNotFound(ServiceError):
    pass


class IncorrectTypeError(ServiceError): 
    pass 


class CashFlowNotFound(ServiceError): 
    pass 


class CashFlowNotFound(ServiceError): 
    pass 


class IncorrectDatetimeFormat(ServiceError): 
    pass 
