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
        method="POST",
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
    ), 
    RequestTestCase(
        method="POST",
        url="/status/", 
        headers={},
        data={
            "status_name": "Хобби"
        }, 
        expected_status=status.HTTP_400_BAD_REQUEST,
        expected_data={
            "status": "Error", 
            "message": "CashStatus with name=Хобби already exists."
        }
    )
]


TEST_CASH_STATUS_ROUTER_UPDATE = [
    RequestTestCase(
        method="PATCH",
        url="/status/1", 
        headers={},
        data={
            "status_name": "Хобби++"
        }, 
        expected_status=status.HTTP_200_OK,
        expected_data={
            "status": "Success", 
            "message": None
        }
    ), 
    RequestTestCase(
        method="PATCH",
        url="/status/33", 
        headers={},
        data={
            "status_name": "Хобби++"
        }, 
        expected_status=status.HTTP_400_BAD_REQUEST,
        expected_data={
            "status": "Error", 
            "message": "CashStatus with id=33 not found."
        }
    ), 
    RequestTestCase(
        method="PATCH",
        url="/status/1", 
        headers={},
        data={
            "status_name": "Налог"
        }, 
        expected_status=status.HTTP_400_BAD_REQUEST,
        expected_data={
            "status": "Error", 
            "message": "CashStatus with name=Налог already exists."
        }
    )
]

TEST_CASH_STATUS_ROUTER_DELETE = [
    RequestTestCase(
        method="DELETE", 
        url="/status/1",
        headers={},
        data={}, 
        expected_status=status.HTTP_200_OK, 
        expected_data={
            "status": "Success", 
            "message": None
        }
    ), 
    RequestTestCase(
        method="DELETE", 
        url="/status/1",
        headers={},
        data={}, 
        expected_status=status.HTTP_400_BAD_REQUEST, 
        expected_data={
            "status": "Error", 
            "message": "CashStatus with id=1 not found."
        }
    )
]
