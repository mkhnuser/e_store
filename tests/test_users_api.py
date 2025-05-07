import os

import pytest
import pytest_asyncio
from httpx import AsyncClient

from src.validation_models import UserValidationModelBase, RoleValidationModelOut


@pytest_asyncio.fixture
async def client(base_async_http_client: AsyncClient):
    base_async_http_client.base_url = (
        str(base_async_http_client.base_url) + os.environ["APP_ROUTERS_USERS_PREFIX"]
    )
    yield base_async_http_client


@pytest.fixture
def user_validation_model():
    yield UserValidationModelBase(
        email="test@test.com",
        phone_number="+375000000000",
        first_name="Gringo",
        last_name="Bongo",
        roles=[
            RoleValidationModelOut(
                id=1, name="customer", description="A plain customer."
            )
        ],
    )


@pytest.mark.asyncio
async def test_get_all_users_returns_200_status_code(client: AsyncClient):
    response = await client.get(os.environ["APP_API_PATHS_USERS_GET_ALL_USERS"])
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_all_users_returns_json_array(client: AsyncClient):
    response = await client.get(os.environ["APP_API_PATHS_USERS_GET_ALL_USERS"])
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_post_user_returns_200_status_code(
    client: AsyncClient, user_validation_model: UserValidationModelBase
):
    response = await client.post(
        os.environ["APP_API_PATHS_USERS_POST_USER"],
        json=user_validation_model.model_dump(),
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_post_user_returns_422_status_code_if_request_has_no_body(
    client: AsyncClient,
):
    response = await client.post(os.environ["APP_API_PATHS_USERS_POST_USER"])
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_post_user_return_json_object(
    client: AsyncClient, user_validation_model: UserValidationModelBase
):
    response = await client.post(
        os.environ["APP_API_PATHS_USERS_POST_USER"],
        json=user_validation_model.model_dump(),
    )
    assert isinstance(response.json(), dict)


@pytest.mark.asyncio
async def test_post_user_returns_user_id(
    client: AsyncClient, user_validation_model: UserValidationModelBase
):
    response = await client.post(
        os.environ["APP_API_PATHS_USERS_POST_USER"],
        json=user_validation_model.model_dump(),
    )
    assert "id" in response.json()


@pytest.mark.asyncio
async def test_post_user_returns_user_data(
    client: AsyncClient, user_validation_model: UserValidationModelBase
):
    response = await client.post(
        os.environ["APP_API_PATHS_USERS_POST_USER"],
        json=user_validation_model.model_dump(),
    )
    data = response.json()
    del data["id"]
    assert data == user_validation_model.model_dump()
