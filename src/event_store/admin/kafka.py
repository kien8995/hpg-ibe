"""
    kafka helper functions
"""
import sys

from confluent_kafka import Consumer, KafkaException, KafkaError
from confluent_kafka.admin import AdminClient, NewTopic
from config import app_config

DEFAULT_SERVER = app_config['kafka']['producer']['default-server']
RESULT_TOPIC = app_config['kafka']['producer']['result-topic']


def get_list_topics(admin_client: AdminClient) -> dict:
    """get list kafka topic

    Args:
        admin_client (AdminClient): kafka AdminClient instance

    Returns:
        dict: Map of topics indexed by the topic name. Value is TopicMetadata object.
    """
    return admin_client.list_topics().topics


def create_new_topic(admin_client: AdminClient, topic_name: str):
    """create new kafka topic

    Args:
        admin_client (AdminClient): kafka AdminClient instance
        topic_name (str): topic name
    """
    topic_list = [NewTopic(topic_name, 1, 1)]
    admin_client.create_topics(topic_list)


def create_new_topics(admin_client: AdminClient, topic_names: list[str]):
    """create new kafka topic

    Args:
        admin_client (AdminClient): kafka AdminClient instance
        topic_names (list[str]): list topic name
    """
    topic_list = []
    for _, val in enumerate(topic_names):
        topic_list.append(NewTopic(val, 1, 1))
    admin_client.create_topics(topic_list)


def delete_topics(admin_client: AdminClient, topic_names: list[str]):
    """delete kafka topic

    Args:
        admin_client (AdminClient): kafka AdminClient instance
        topic_names (list[str]): list topic name
    """
    fs = admin_client.delete_topics(topic_names, operation_timeout=30)

    # Wait for operation to finish.
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print(f"Topic {topic} deleted")
        except Exception as ex:
            print(f"Failed to delete topic {topic}: {ex}")


def print_consumer_value(consumer: Consumer, topics: list[str] = None):
    """print kafka consumer value

    Args:
        consumer (Consumer): kafka consumer
        topics (list[str], optional): list topic name. Defaults to None.

    Raises:
        KafkaException: _description_
    """
    if topics is None:
        topics = [RESULT_TOPIC]

    try:
        consumer.subscribe(topics)

        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF: # pylint: disable=protected-access
                    # End of partition event
                    sys.stderr.write(f'%% {msg.topic()} [{msg.partition()}] reached end at offset {msg.offset()}\n')
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(msg.value())
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()


if __name__ == "__main__":
    # admin_client = AdminClient({"bootstrap.servers": ','.join(DEFAULT_SERVER)})
    # print(get_list_topics(admin_client))

    conf = {'bootstrap.servers': ','.join(DEFAULT_SERVER),
            'group.id': "foo",
            'enable.auto.commit': False,
            'auto.offset.reset': 'earliest'}
    kafka_consumer = Consumer(conf)

    print_consumer_value(kafka_consumer)
