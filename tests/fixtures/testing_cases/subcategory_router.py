from fastapi import status

from tests.utils import RequestTestCase

TEST_SUBCATEGORY_ROUTER_GET = [
    RequestTestCase(
        url="/subcategory/", 
        headers={}, 
        data={}, 
        expected_data=[
            {'subcategory_id': 1, 'subcategory_name': 'VPS'}, 
            {'subcategory_id': 2, 'subcategory_name': 'Proxy'}, 
            {'subcategory_id': 3, 'subcategory_name': 'Farpost'}, 
            {'subcategory_id': 4, 'subcategory_name': 'Avito'}
        ]
    )
]

TEST_SUBCATEGORY_ROUTER_CREATE = [
    RequestTestCase(
        method="POST",
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
    ), 
    RequestTestCase(
        method="POST",
        url="/subcategory/", 
        headers={}, 
        data={
            "parent_category": 2,
            "subcategory_name": "OLX"
        }, 
        expected_status=status.HTTP_400_BAD_REQUEST, 
        expected_data={
            "status": "Error", 
            "message": "SubCategory with name=OLX already exists."
        }
    ), 
]

TEST_SUBCATEGORY_ROUTER_UPDATE = [
    RequestTestCase(
        method="PATCH",
        url="/subcategory/3", 
        headers={}, 
        data={
            "subcategory_name": "OLX(UK)"
        }, 
        expected_status=status.HTTP_200_OK, 
        expected_data={
            "status": "Success", 
            "message": None,
        }
    ), 
    RequestTestCase(
        method="PATCH",
        url="/subcategory/3", 
        headers={}, 
        data={
            "parent_category": 33,
            "subcategory_name": "OLX(US)"
        }, 
        expected_status=status.HTTP_400_BAD_REQUEST, 
        expected_data={
            "status": "Error", 
            "message": "Category with id=33 not found.",
        }
    ), 
    RequestTestCase(
        method="PATCH",
        url="/subcategory/3", 
        headers={}, 
        data={
            "subcategory_name": "Avito"
        }, 
        expected_status=status.HTTP_400_BAD_REQUEST, 
        expected_data={
            "status": "Error", 
            "message": "Subcategory with name=Avito already exists.",
        }
    )
]

TEST_SUBCATEGORY_ROUTER_DELETE = [
    RequestTestCase(
        method="DELETE",
        url="/subcategory/3", 
        headers={}, 
        data={}, 
        expected_status=status.HTTP_200_OK, 
        expected_data={
            "status": "Success", 
            "message": None,
        }
    ), 
    RequestTestCase(
        method="DELETE",
        url="/subcategory/3", 
        headers={}, 
        data={}, 
        expected_status=status.HTTP_400_BAD_REQUEST, 
        expected_data={
            "status": "Error", 
            "message": "SubCategory with id=3 not found.",
        }
    )
]
