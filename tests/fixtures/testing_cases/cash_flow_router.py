from datetime import datetime, timezone

from fastapi import status

from tests.utils import RequestTestCase

TEST_CASH_FLOW_ROUTER_GET = [
    RequestTestCase(
        url="/cash-flow/", 
        headers={}, 
        data={},
        expected_data=[]
    )
]

TEST_CASH_FLOW_ROUTER_CREATE = [
    RequestTestCase(
        method="POST",
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
    ), 
    RequestTestCase(
        method="POST",
        url="/cash-flow/", 
        headers={}, 
        data={
            "cash_status": 2,
            "cash_type": 1,
            "category": 2,
            "amount": 55.3,
            "comment": "Some text"
        }, 
        expected_status=status.HTTP_400_BAD_REQUEST, 
        expected_data={
            "status": "Error", 
            "message": "Category with id=2 not belong to CashType with id=1."
        }
    ), 
    RequestTestCase(
        method="POST",
        url="/cash-flow/", 
        headers={}, 
        data={
            "cash_status": 2,
            "cash_type": 2,
            "category": 1,
            "amount": 55.3,
            "comment": "Some text2"
        }, 
        expected_status=status.HTTP_201_CREATED, 
        expected_data={
            "status": "Success", 
            "message": None
        }
    )
]

TEST_CASH_FLOW_GET_WITH_SPECIFICATIONS = [
    RequestTestCase(
        method="POST", 
        url="/cash-flow/specifications", 
        data={
            "cash_type": 1
        }, 
        expected_status=status.HTTP_200_OK, 
        expected_data=[
            {
                'create_utc': datetime.now(timezone.utc).strftime("%d.%m.%Y"), 
                'cash_flow_id': 1, 
                'cash_status': {'status_id': 2, 'status_name': 'Личное'}, 
                'cash_type': {'type_id': 2, 'type_name': 'Списание'}, 
                'category': {
                    'caterogy_id': 1, 
                    'category_name': 'Инфраструктура', 
                    'subcategories': [
                        {'subcategory_id': 1, 'subcategory_name': 'VPS'}, 
                        {'subcategory_id': 2, 'subcategory_name': 'Proxy'}
                    ]
                }, 
                'amount': 55.3, 
                'comment': 'Some text'
            }, 
            {
                'create_utc': datetime.now(timezone.utc).strftime("%d.%m.%Y"), 
                'cash_flow_id': 2, 
                'cash_status': {'status_id': 2, 'status_name': 'Личное'}, 
                'cash_type': {'type_id': 2, 'type_name': 'Списание'}, 
                'category': {
                    'caterogy_id': 1, 
                    'category_name': 'Инфраструктура', 
                    'subcategories': [
                        {'subcategory_id': 1, 'subcategory_name': 'VPS'}, 
                        {'subcategory_id': 2, 'subcategory_name': 'Proxy'}
                    ]
                }, 
                'amount': 55.3, 
                'comment': 'Some text2'
            }
        ]
    )
]

TEST_CASH_FLOW_ROUTER_UPDATE = [
    RequestTestCase(
        method="PATCH",
        url="/cash-flow/1", 
        headers={}, 
        data={
            "cash_status": 2,
            "cash_type": 2,
            "category": 2,
            "amount": 53.3,
            "comment": "Some text2"
        }, 
        expected_status=status.HTTP_200_OK, 
        expected_data={
            "status": "Success", 
            "message": None
        }
    ), 
    RequestTestCase(
        method="PATCH",
        url="/cash-flow/33", 
        headers={}, 
        data={
            "cash_status": 2,
            "cash_type": 2,
            "category": 1,
            "amount": 53.3,
            "comment": "Some text2"
        }, 
        expected_status=status.HTTP_400_BAD_REQUEST, 
        expected_data={
            "status": "Error", 
            "message": "CashFlow with id=33 not found."
        }
    ), 
    RequestTestCase(
        method="PATCH",
        url="/cash-flow/33", 
        headers={}, 
        data={
            "cash_status": 2,
            "cash_type": 1,
            "category": 2,
            "amount": 53.3,
            "comment": "Some text2"
        }, 
        expected_status=status.HTTP_400_BAD_REQUEST, 
        expected_data={
            "status": "Error", 
            "message": "Category with id=2 not belong to CashType with id=1."
        }
    ), 
]

TEST_CASH_FLOW_ROUTER_DELETE = [
    RequestTestCase(
        method="DELETE",
        url="/cash-flow/1", 
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
        url="/cash-flow/1", 
        headers={}, 
        data={}, 
        expected_status=status.HTTP_400_BAD_REQUEST, 
        expected_data={
            "status": "Error", 
            "message": "CashFlow with id=1 not found."
        }
    )
]
