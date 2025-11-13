import pytest
from httpx import AsyncClient

from tests.fixtures import testing_cases
from tests.integration.utils.mixins import AssertMixin
from tests.utils import RequestTestCase, prepare_payload


class TestCompanyRouter(AssertMixin):
    @pytest.mark.parametrize("case", testing_cases.TEST_CASH_TYPE_ROUTER_GET)
    async def test_get(self, case: RequestTestCase, async_client: AsyncClient) -> None: 
        response = await async_client.request(case.method, case.url, json=case.data, headers=case.headers)
        self.assertEqual(response.status_code, case.expected_status) 
        self.assertEqual(prepare_payload(response)["data"], case.expected_data)

    @pytest.mark.parametrize("case", testing_cases.TEST_CASH_TYPE_ROUTER_CREATE)
    async def test_create(self, case: RequestTestCase, async_client: AsyncClient) -> None:
        response = await async_client.request(case.method, case.url, json=case.data, headers=case.headers)
        self.assertEqual(response.status_code, case.expected_status)
        self.assertEqual(prepare_payload(response), case.expected_data)

    @pytest.mark.parametrize("case", testing_cases.TEST_CASH_TYPE_ROUTER_UPDATE)
    async def test_update(self, case: RequestTestCase, async_client: AsyncClient) -> None: 
        response = await async_client.request(case.method, case.url, json=case.data, headers=case.headers)
        self.assertEqual(response.status_code, case.expected_status)
        self.assertEqual(prepare_payload(response), case.expected_data) 
