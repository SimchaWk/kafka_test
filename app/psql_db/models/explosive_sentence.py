from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.psql_db.models import Base


class ExplosiveSentence(Base):
    __tablename__ = 'explosive_sentences'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email_id = Column(UUID(as_uuid=True), ForeignKey('emails.id'))
    content = Column(String, nullable=False)

    email = relationship("Email", back_populates="explosive_sentences")
