import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session as SQLAlchemySession, sessionmaker


engine = create_engine(os.environ["APP_DATABASE_URL"], echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session() -> Generator[SQLAlchemySession, None, None]:
    db_session = Session()
    try:
        yield db_session
    finally:
        db_session.close()
