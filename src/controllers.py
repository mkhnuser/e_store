from sqlalchemy.orm import Session
from .db_models import UserDatabaseModel


async def get_all_users(db_session: Session) -> list[UserDatabaseModel]:
    await db_session.scalars()
