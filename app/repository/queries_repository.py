from typing import Optional, Dict, Any, List
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select

from app.psql_db.connection import session_maker
from app.psql_db.models import Email, ExplosiveSentence, HostageSentence


def email_by_address(email_address: str) -> Optional[Email]:
    with session_maker() as session:
        try:
            query = (
                select(Email)
                .options(
                    joinedload(Email.location),
                    joinedload(Email.device_info),
                    joinedload(Email.explosive_sentences),
                    joinedload(Email.hostage_sentences)
                )
                .where(Email.email == email_address)
            )
            email = session.execute(query).unique().scalar_one_or_none()

            if not email:
                return None

            return email

        except Exception as e:
            session.rollback()
            print(e)


def get_all_sentences() -> List[str]:
    with session_maker() as session:
        try:
            explosive_query = select(ExplosiveSentence.content)
            hostage_query = select(HostageSentence.content)

            explosive_sentences = session.execute(explosive_query).scalars().all()
            hostage_sentences = session.execute(hostage_query).scalars().all()

            return explosive_sentences + hostage_sentences

        except Exception as e:
            session.rollback()
            print(e)
            return []
