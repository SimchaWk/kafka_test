from typing import Dict
from dotenv import load_dotenv
import os

from app.kafka_settings.producer import produce

load_dotenv(verbose=True)
new_member_topic = os.environ['ALL_MESSAGES_TOPIC']


def produce_new_rew_data(data: Dict) -> bool:
    return produce(
        topic=new_member_topic,
        message=data,
        key=data.get('id', None)
    )
