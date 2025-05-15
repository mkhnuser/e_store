import os
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession


engine = create_async_engine(os.environ["APP_DATABASE_URL"], echo=False)
Session = async_sessionmaker(engine, expire_on_commit=False)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = Session()
    try:
        yield async_session
    finally:
        await async_session.close()
