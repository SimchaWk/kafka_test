from dotenv import load_dotenv
import os

from app.kafka_settings.consumer import consume
from app.services.raw_data_service import handle_raw_data

load_dotenv(verbose=True)
all_messages_topic = os.environ['ALL_MESSAGES_TOPIC']

def consume_rew_data() -> None:
     consume(
        topic=all_messages_topic,
        function=handle_raw_data
    )

if __name__ == '__main__':
    consume_rew_data()