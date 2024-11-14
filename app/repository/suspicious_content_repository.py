from typing import Optional
from sqlalchemy.exc import SQLAlchemyError

from app.psql_db.connection import session_maker
from app.psql_db.models import Location, DeviceInfo, Email
from app.services.parse_models_service import parse_json_to_models


def save_email_with_relations(email_model: Email) -> Optional[Email]:
    with session_maker() as session:
        try:
            session.add(email_model)
            session.commit()
            return email_model

        except SQLAlchemyError as e:
            session.rollback()
