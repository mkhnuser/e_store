import pytest_asyncio
from httpx import ASGITransport, AsyncClient


from src.main import app


@pytest_asyncio.fixture
async def base_async_http_client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as c:
        yield c
