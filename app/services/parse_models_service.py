from datetime import datetime
import uuid

from app.psql_db.models import Location, DeviceInfo, Email, ExplosiveSentence, HostageSentence


def create_location(location_data: dict) -> Location:
    return Location(
        id=uuid.uuid4(),
        latitude=location_data.get('latitude'),
        longitude=location_data.get('longitude'),
        city=location_data.get('city'),
        country=location_data.get('country')
    )


def create_device_info(device_info_data: dict) -> DeviceInfo:
    return DeviceInfo(
        id=uuid.uuid4(),
        browser=device_info_data.get('browser'),
        os=device_info_data.get('os'),
        device_id=uuid.UUID(device_info_data.get('device_id'))
    )


def create_sentence(email_id: uuid.UUID, sentences_data: list, topic: str) -> list:
    if topic == "explosive":
        return [
            ExplosiveSentence(email_id=email_id, content=sentence_text)
            for sentence_text in sentences_data
        ]
    elif topic == "hostage":
        return [
            HostageSentence(email_id=email_id, content=sentence_text)
            for sentence_text in sentences_data
        ]
    return []


def create_email(json_data: dict, location: Location, device_info: DeviceInfo) -> Email:
    return Email(
        id=uuid.UUID(json_data.get('id')),
        email=json_data.get('email'),
        username=json_data.get('username'),
        ip_address=json_data.get('ip_address'),
        created_at=datetime.fromisoformat(json_data.get('created_at')),
        location=location,
        device_info=device_info
    )


def parse_json_to_models(json_data, category: str) -> Email:
    location = create_location(json_data.get('location', {}))
    device_info = create_device_info(json_data.get('device_info', {}))

    email = create_email(json_data, location, device_info)

    sentences = create_sentence(email.id, json_data.get('sentences', []), category)
    if category == 'explosive':
        email.explosive_sentences = sentences
    elif category == 'hostage':
        email.hostage_sentences = sentences

    return email
