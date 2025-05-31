from typing import AsyncGenerator

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.validation_models import UserValidationModelIn

from .db_models import RoleDatabaseModel, UserDatabaseModel
from .crypto import hash_password


async def get_users(
    s: AsyncSession,
    limit: int,
    offset: int,
) -> AsyncGenerator[UserDatabaseModel, None]:
    try:
        for user in await s.scalars(
            select(UserDatabaseModel).limit(limit).offset(offset)
        ):
            yield user
    except Exception as e:
        # TODO: IMPLEMENT ERROR HANDLING AND LOGGING.
        print(e)
        raise


async def get_user_by_id(s: AsyncSession, user_id: int) -> UserDatabaseModel:
    try:
        return await s.get_one(UserDatabaseModel, user_id)
    except Exception as e:
        # TODO: IMPLEMENT ERROR HANDLING AND LOGGING.
        print(e)
        raise


async def post_user(
    s: AsyncSession,
    user_model: UserValidationModelIn,
) -> UserDatabaseModel:
    try:
        user_dict = user_model.model_dump()
        password = user_dict.pop("password")
        # TODO: FORGET ABOUT ROLES FOR NOW.
        roles_list = user_dict.pop("roles")
        user = UserDatabaseModel(**user_dict, roles=[])

        # user_roles = [RoleDatabaseModel(**role) for role in roles_list]
        # for role in user_roles:
        #     user.roles.append(role)

        # TODO: THINK ABOUT DELEGATION TO A THREAD?
        user.password = hash_password(password)
        s.add(user)
        await s.commit()
        return user
    except Exception as e:
        # TODO: IMPLEMENT ERROR HANDLING AND LOGGING.
        await s.rollback()
        print(e)
        raise
