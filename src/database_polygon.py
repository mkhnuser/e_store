import asyncio
from dotenv import load_dotenv

is_dotenv_loaded = load_dotenv("./.env.production")
print(is_dotenv_loaded)


from validation_models import UserValidationModelOut
from sqlalchemy import *
from db_models import *
from db import *


async def create_some_users() -> None:
    s = Session()
    users = [
        UserDatabaseModel(email="email@email.com", first_name="Vlad"),
        UserDatabaseModel(email="some@email.com", first_name="John"),
    ]
    for user in users:
        s.add(user)
    await s.commit()


async def get_all_users() -> None:
    s = Session()
    res = await s.scalars(select(UserDatabaseModel))
    for user in res:
        print(user)
    await s.close()


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    await create_some_users()
    await get_all_users()

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


if __name__ == "__main__":
    asyncio.run(main())
