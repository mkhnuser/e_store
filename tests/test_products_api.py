import os

import pytest
import pytest_asyncio
from httpx import AsyncClient


@pytest_asyncio.fixture
async def client(base_async_http_client: AsyncClient):
    base_async_http_client.base_url = (
        str(base_async_http_client.base_url) + os.environ["APP_ROUTERS_PRODUCTS_PREFIX"]
    )
    yield base_async_http_client


@pytest.mark.asyncio
async def test_get_all_products_returns_200_status_code(client: AsyncClient):
    response = await client.get(os.environ["APP_API_PATHS_PRODUCTS_GET_ALL_PRODUCTS"])
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_all_products_returns_json_array(client: AsyncClient):
    response = await client.get(os.environ["APP_API_PATHS_PRODUCTS_GET_ALL_PRODUCTS"])
    assert isinstance(response.json(), list)
