from fastapi import status

from tests.utils import RequestTestCase

TEST_CASH_STATUS_ROUTER_GET_ALL = [
    RequestTestCase(
        url="/status/",
        headers={}, 
        data={}, 
        expected_data=[
            {
                "status_id": 1,
                "status_name": "Бизнес"
            },
            {
                "status_id": 2,
                "status_name": "Личное"
            },
            {
                "status_id": 3,
                "status_name": "Налог"
            }
        ],
        description="Get all default statuses"
    )
]

TEST_CASH_STATUS_ROUTER_CREATE = [
    RequestTestCase(
        url="/status/", 
        headers={},
        data={
            "status_name": "Хобби"
        }, 
        expected_status=status.HTTP_201_CREATED,
        expected_data={
            "status": "Success", 
            "message": None
        },
        description="Create new status"
    )
]
