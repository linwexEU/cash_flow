from fastapi import status

from tests.utils import RequestTestCase

TEST_CATEGORY_ROUTER_GET = [
    RequestTestCase(
        url="/category/", 
        haeders={}, 
        data={}, 
        expected_data=[
            {
                "caterogy_id": 1,
                "category_name": "Инфраструктура”",
                "cash_type": {
                    "type_id": 2,
                    "type_name": "Списание"
                },
                "subcategories": [
                    {
                        "subcategory_id": 1,
                        "subcategory_name": "VPS"
                    },
                    {
                        "subcategory_id": 2,
                        "subcategory_name": "Proxy"
                    }
                ]
            },
            {
                "caterogy_id": 2,
                "category_name": "Маркетинг",
                "cash_type": {
                    "type_id": 2,
                    "type_name": "Списание"
                },
                "subcategories": [
                    {
                        "subcategory_id": 3,
                        "subcategory_name": "Farpost"
                    },
                    {
                        "subcategory_id": 4,
                        "subcategory_name": "Avito"
                    }
                ]
            }
        ]
    )
]

TEST_CATEGORY_ROUTER_CREATE = [
    RequestTestCase(
        url="/category/", 
        headers={}, 
        data={
            "cash_type": 1,
            "category_name": "Крипта"
        },
        expected_status=status.HTTP_201_CREATED, 
        expected_data={
            "status": "Success", 
            "message": None
        }
    )
]
