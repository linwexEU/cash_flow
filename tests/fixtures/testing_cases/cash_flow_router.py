from fastapi import status

from tests.utils import RequestTestCase

TEST_CASH_FLOW_ROUTER_GET = [
    RequestTestCase(
        url="/cash-flow/", 
        headers={}, 
        data={}, 
        exprected_data=[]
    )
]

TEST_CASH_FLOW_ROUTER_CREATE = [
    RequestTestCase(
        url="/cash-flow/", 
        headers={}, 
        data={
            "cash_status": 2,
            "cash_type": 2,
            "category": 1,
            "amount": 55.3,
            "comment": "Some text"
        }, 
        expected_status=status.HTTP_201_CREATED, 
        expected_data={
            "status": "Success", 
            "message": None
        }
    )
]
