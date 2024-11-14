from dotenv import load_dotenv
import os

from app.kafka_settings.consumer import consume
from app.services.suspicious_content_service import save_hostage_sentences, save_hostage_sentences2

load_dotenv(verbose=True)
messages_hostage_topic = os.environ['MESSAGES_EXPLOSIVE_TOPIC']


def consume_hostage() -> None:
    consume(
        topic=messages_hostage_topic,
        function=save_hostage_sentences2
    )


if __name__ == '__main__':
    consume_hostage()
