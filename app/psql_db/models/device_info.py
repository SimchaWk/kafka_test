from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.psql_db.models import Base


class DeviceInfo(Base):
    __tablename__ = 'devices_info'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    browser = Column(String, nullable=False)
    os = Column(String, nullable=False)
    device_id = Column(UUID(as_uuid=True), nullable=False, unique=True)

    email = relationship("Email", back_populates="device_info")
