from sqlalchemy import Column, String, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.psql_db.models import Base


class Location(Base):
    __tablename__ = 'locations'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)

    email = relationship("Email", back_populates="location")
