from typing import Any

from fastapi import status
from pydantic import BaseModel


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
