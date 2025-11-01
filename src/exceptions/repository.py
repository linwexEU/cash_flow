

class RepositoryError(Exception): 
    pass 


class RepositoryIntegrityError(RepositoryError): 
    pass 


class NotFoundError(RepositoryError): 
    pass 
