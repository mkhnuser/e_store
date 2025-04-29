from sqlalchemy.orm import Session
from ..sqlalchemy_models.customers_models import Customer


def get_all_customers(db_session: Session) -> list[Customer]:
    return db_session.query(Customer).all()
