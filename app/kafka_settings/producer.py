import json
import os
from typing import Any
from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv(verbose=True)


def produce(topic: str, message: Any, key: str = None) -> bool:
    try:
        producer = KafkaProducer(
            bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
            value_serializer=lambda v: json.dumps(v).encode()
        )
        producer.send(
            topic=topic,
            value=message,
            key=key.encode('utf-8')
        )
        return True
    except Exception as e:
        print(f'Error sending message to topic {topic}: {str(e)}')
        return False
