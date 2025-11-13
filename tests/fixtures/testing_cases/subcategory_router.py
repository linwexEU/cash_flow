from fastapi import status

from tests.utils import RequestTestCase

TEST_SUBCATEGORY_ROUTER_GET = [
    RequestTestCase(
        url="/subcategory/", 
        headers={}, 
        data={}, 
        exprected_data=[
            {
                "subcategory_id": 1,
                "subcategory_name": "VPS"
            },
            {
                "subcategory_id": 2,
                "subcategory_name": "Proxy"
            },
            {
                "subcategory_id": 3,
                "subcategory_name": "Farpost"
            },
            {
                "subcategory_id": 4,
                "subcategory_name": "Avito"
            }
        ]
    )
]

TEST_SUBCATEGORY_ROUTER_CREATE = [
    RequestTestCase(
        url="/subcategory/", 
        headers={}, 
        data={
            "parent_category": 2,
            "subcategory_name": "OLX"
        }, 
        expected_status=status.HTTP_201_CREATED, 
        expected_data={
            "status": "Success", 
            "message": None
        }
    )
]
