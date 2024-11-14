from datetime import datetime
import uuid

from app.psql_db.models import Location, DeviceInfo, Email, Sentence


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


def create_sentences(email_id: uuid.UUID, sentences_data: list) -> list[Sentence]:
    return [
        Sentence(email_id=email_id, content=sentence_text)
        for sentence_text in sentences_data
    ]


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


def parse_json_to_models(json_data: dict) -> Email:
    location = create_location(json_data.get('location', {}))
    device_info = create_device_info(json_data.get('device_info', {}))

    email = create_email(json_data, location, device_info)
    email.sentences = create_sentences(email.id, json_data.get('sentences', []))

    return email


if __name__ == '__main__':
    m = {
        "_id": {
            "$oid": "6735b73330255ba850f033c1"
        },
        "id": "55e9311d-7ce7-4c98-8bd8-29cb894447ed",
        "email": "tonywilliams@example.com",
        "username": "nathan39",
        "ip_address": "175.246.239.218",
        "created_at": "2024-10-30T05:29:51",
        "location": {
            "latitude": -18.27867,
            "longitude": -139.102917,
            "city": "East Mary",
            "country": "YE"
        },
        "device_info": {
            "browser": "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 6.0; Trident/5.1)",
            "os": "MacOS",
            "device_id": "1e9fdc1e-c59a-408a-8c86-340728f0a135"
        },
        "sentences": [
            "New office somebody daughter Democrat.",
            "Just goal former hand rest level.",
            "Away explain current grow technology."
        ]
    }
    res = parse_json_to_models(m)
    print(res)
