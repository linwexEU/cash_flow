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
                "category_name": "Инфраструктура",
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
        method="POST",
        url="/category/", 
        headers={}, 
        data={
            "cash_type": 2,
            "category_name": "Крипта"
        },
        expected_status=status.HTTP_201_CREATED, 
        expected_data={
            "status": "Success", 
            "message": None
        }
    ), 
    RequestTestCase(
        method="POST",
        url="/category/", 
        headers={}, 
        data={
            "cash_type": 99,
            "category_name": "Крипта++"
        },
        expected_status=status.HTTP_400_BAD_REQUEST, 
        expected_data={
            "status": "Error", 
            "message": "CashType with id=99 does not exist."
        }
    ), 
    RequestTestCase(
        method="POST",
        url="/category/", 
        headers={}, 
        data={
            "cash_type": 2,
            "category_name": "Крипта"
        },
        expected_status=status.HTTP_400_BAD_REQUEST, 
        expected_data={
            "status": "Error", 
            "message": "Category with name=Крипта already exists."
        }
    ),
]


TEST_CATEGORY_ROUTER_UPDATE = [
    RequestTestCase(
        method="PATCH",
        url="/category/1", 
        headers={}, 
        data={
            "category_name": "Инфраструктура++"
        },
        expected_status=status.HTTP_200_OK, 
        expected_data={
            "status": "Success", 
            "message": None
        }
    ), 
    RequestTestCase(
        method="PATCH",
        url="/category/1", 
        headers={}, 
        data={
            "category_name": "Маркетинг"
        },
        expected_status=status.HTTP_400_BAD_REQUEST, 
        expected_data={
            "status": "Error", 
            "message": "Category with name=Маркетинг already exists."
        }
    ),
    RequestTestCase(
        method="PATCH",
        url="/category/1", 
        headers={}, 
        data={
            "cash_type": 55,
            "category_name": "Маркетинг+Cash"
        },
        expected_status=status.HTTP_400_BAD_REQUEST, 
        expected_data={
            "status": "Error", 
            "message": "CashType with id=55 not found."
        }
    )
]

TEST_CATEGORY_ROUTER_DELETE = [
    RequestTestCase(
        method="DELETE",
        url="/category/1", 
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
        url="/category/1", 
        headers={}, 
        data={},
        expected_status=status.HTTP_400_BAD_REQUEST, 
        expected_data={
            "status": "Error", 
            "message": "Category with id=1 not found."
        }
    )
]
