import pytest


@pytest.mark.asyncio
async def test_root(base_async_http_client):
    response = await base_async_http_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"success": True}
