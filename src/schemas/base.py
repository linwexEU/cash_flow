from pydantic import BaseModel

from src.models.enums import ResponseStatus


class BaseResponse(BaseModel): 
    status: ResponseStatus 
    message : str | None = None
