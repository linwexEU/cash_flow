from fastapi import status

from tests.utils import RequestTestCase

TEST_CASH_TYPE_ROUTER_GET = [
    RequestTestCase(
        url="/type/", 
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
        method="POST",
        url="/type/", 
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
    ), 
    RequestTestCase(
        method="POST",
        url="/type/", 
        headers={}, 
        data={
            "type_name": "Кешбек"
        }, 
        expected_status=status.HTTP_400_BAD_REQUEST, 
        expected_data={
            "status": "Error", 
            "message": "CashType with name=Кешбек already exists."
        }
    ), 
    
]

TEST_CASH_TYPE_ROUTER_UPDATE = [
    RequestTestCase(
        method="PATCH", 
        url="/type/1",
        headers={},
        data={
            "type_name": "Пополнение+"
        }, 
        expected_status=status.HTTP_200_OK, 
        expected_data={
            "status": "Success", 
            "message": None
        }
    )
]
