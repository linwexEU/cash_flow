from typing import Any, Sequence

from fastapi import status
from pydantic import BaseModel
from requests import Response


class TestDescription(BaseModel):
    description: str = "" 


class TestExpectation(BaseModel): 
    expected_status: int = status.HTTP_200_OK 
    expected_data: Any = None


class BaseTestCase(TestDescription, TestExpectation): 
    data: dict | None = None 


class RequestTestCase(BaseTestCase): 
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
