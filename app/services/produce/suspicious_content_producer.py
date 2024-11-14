from typing import Dict

from app.kafka_settings.producer import produce


def produce_suspicious_content(topic: str, data: Dict) -> bool:
    return produce(
        topic=topic,
        message=data,
        key=data['id']
    )
