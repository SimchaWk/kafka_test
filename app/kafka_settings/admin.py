import os
from dotenv import load_dotenv
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

load_dotenv(verbose=True)


def init_topics():
    client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
    new_member_topic = NewTopic(
        name=os.environ['NEW_MEMBER_TOPIC'],
        num_partitions=int(os.environ['NUM_PARTITIONS']),
        replication_factor=int(os.environ['REPLICATION_FACTOR'])
    )
    try:
        client.create_topics([new_member_topic])
        print('Topics created successfully!')
    except TopicAlreadyExistsError as e:
        print(e)
    except Exception as e:
        print(f'Error creating topics: {e}')
    finally:
        client.close()