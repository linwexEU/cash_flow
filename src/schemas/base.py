from pydantic import BaseModel

from src.models.enums import ResponseStatus


class BaseResponse(BaseModel): 
    Status: ResponseStatus 
    Message : str | None = None
