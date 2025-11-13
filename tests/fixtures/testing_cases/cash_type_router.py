from fastapi import status

from tests.utils import RequestTestCase
from tests.constants import BASE_ENDPOINT_URL 

TEST_CASH_TYPE_ROUTER_GET = [
    RequestTestCase(
        url=f"{BASE_ENDPOINT_URL}/type", 
        headers={}, 
        data={},
        expected_data=[
            {
                "type_id": 1,
                "type_name": "Пополнение"
            },
            {
                "type_id": 2,
                "type_name": "Списание"
            }
        ], 
        description="Get all default types"
    )
]

TEST_CASH_TYPE_ROUTER_CREATE = [
    RequestTestCase(
        url=f"{BASE_ENDPOINT_URL}/type", 
        headers={}, 
        data={
            "type_name": "Кешбек"
        }, 
        expected_status=status.HTTP_201_CREATED, 
        expected_data={
            "status": "Success", 
            "message": None
        }, 
        description="Create new type"
    )
]
