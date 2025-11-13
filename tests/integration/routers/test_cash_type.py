import pytest
from httpx import AsyncClient

from tests.fixtures import testing_cases
from tests.integration.utils.mixins import AssertMixin
from tests.utils import RequestTestCase, prepare_payload


class TestCompanyRouter(AssertMixin):
    @pytest.mark.parametrize("case", testing_cases.TEST_CASH_TYPE_ROUTER_CREATE)
    async def test_create(self, case: RequestTestCase, async_client: AsyncClient):
        response = await async_client.post(case.url, json=case.data, headers=case.headers)
        self.assertEqual(response.status_code, case.expected_status)
        self.assertEqual(prepare_payload(response), case.expected_data)
