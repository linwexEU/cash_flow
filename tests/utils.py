from typing import Any, Sequence, Literal
from contextlib import AbstractContextManager, nullcontext

from fastapi import status
from pydantic import BaseModel, ConfigDict
from requests import Response


class BaseConfig(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)


class TestDescription(BaseConfig):
    description: str = "" 


class TestExpectation(BaseConfig): 
    expected_error: AbstractContextManager = nullcontext()
    expected_status: int = status.HTTP_200_OK 
    expected_data: Any = None


class BaseTestCase(TestDescription, TestExpectation): 
    data: dict | None = None 


class RequestTestCase(BaseTestCase): 
    method: Literal["GET", "POST", "PATCH", "PUT", "DELETE"] = "GET"
    url: str
    headers: dict | None = None


def prepare_payload(response: Response, exclude: Sequence[str] | None = None) -> dict: 
    """Extracts the payload from the response."""
    payload = response.json()
    if payload is None: 
        return {} 
    
    if exclude is None:
        return payload
    
    for key in payload: 
        payload.pop(key) 

    return payload
