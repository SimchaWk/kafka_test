from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.psql_db.models import Base


class Email(Base):
    __tablename__ = 'emails'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    location_id = Column(UUID(as_uuid=True), ForeignKey('locations.id'))
    device_info_id = Column(UUID(as_uuid=True), ForeignKey('devices_info.id'))

    location = relationship("Location", back_populates="email")
    device_info = relationship("DeviceInfo", back_populates="email")

    hostage_sentences = relationship("HostageSentence", back_populates="email")
    explosive_sentences = relationship("ExplosiveSentence", back_populates="email")

    def __repr__(self):
        return f"<Email(email='{self.email}', username='{self.username}')>"
