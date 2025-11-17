from httpx import AsyncClient
import pytest

from tests.integration.utils.mixins import AssertMixin
from tests.fixtures import testing_cases 
from tests.utils import prepare_payload, RequestTestCase


class TestCategory(AssertMixin): 
    @pytest.mark.parametrize("case", testing_cases.TEST_CATEGORY_ROUTER_GET)
    async def test_get(self, case: RequestTestCase, async_client: AsyncClient) -> None: 
        response = await async_client.request(case.method, case.url, json=case.data, headers=case.headers)
        self.assertEqual(response.status_code, case.expected_status)
        self.assertEqual(prepare_payload(response)["data"], case.expected_data)

    @pytest.mark.parametrize("case", testing_cases.TEST_CATEGORY_ROUTER_CREATE)
    async def test_create(self, case: RequestTestCase, async_client: AsyncClient) -> None: 
        response = await async_client.request(case.method, case.url, json=case.data, headers=case.headers)
        self.assertEqual(response.status_code, case.expected_status)
        self.assertEqual(prepare_payload(response), case.expected_data)

    @pytest.mark.parametrize("case", testing_cases.TEST_CATEGORY_ROUTER_UPDATE)
    async def test_update(self, case: RequestTestCase, async_client: AsyncClient) -> None: 
        response = await async_client.request(case.method, case.url, json=case.data, headers=case.headers)
        self.assertEqual(response.status_code, case.expected_status)
        self.assertEqual(prepare_payload(response), case.expected_data)

    @pytest.mark.parametrize("case", testing_cases.TEST_CATEGORY_ROUTER_DELETE)
    async def test_delete(self, case: RequestTestCase, async_client: AsyncClient) -> None: 
        response = await async_client.request(case.method, case.url, json=case.data, headers=case.headers)
        self.assertEqual(response.status_code, case.expected_status)
        self.assertEqual(prepare_payload(response), case.expected_data)
     