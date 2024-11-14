from dotenv import load_dotenv
import os

from app.kafka_settings.consumer import consume
from app.services.suspicious_content_service import save_explosive_sentences

load_dotenv(verbose=True)
messages_explosive_topic = os.environ['MESSAGES_EXPLOSIVE_TOPIC']


def consume_explosive() -> None:
    consume(
        topic=messages_explosive_topic,
        function=save_explosive_sentences
    )


if __name__ == '__main__':
    consume_explosive()
