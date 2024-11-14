from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
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
    sentences = relationship("Sentence", back_populates="email")

    def __repr__(self):
        return f"<Email(email='{self.email}', username='{self.username}')>"


class Location(Base):
    __tablename__ = 'locations'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)

    email = relationship("Email", back_populates="location")


class DeviceInfo(Base):
    __tablename__ = 'devices_info'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    browser = Column(String, nullable=False)
    os = Column(String, nullable=False)
    device_id = Column(UUID(as_uuid=True), nullable=False, unique=True)

    email = relationship("Email", back_populates="device_info")


class Sentence(Base):
    __tablename__ = 'sentences'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email_id = Column(UUID(as_uuid=True), ForeignKey('emails.id'))
    content = Column(String, nullable=False)

    email = relationship("Email", back_populates="sentences")
