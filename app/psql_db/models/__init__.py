from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .device_info import DeviceInfo
from .email_model import Email
from .location import Location
from .sentence import Sentence
