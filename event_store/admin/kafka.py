import sys

from confluent_kafka import Consumer, KafkaException, KafkaError
from confluent_kafka.admin import AdminClient, NewTopic
from config import config

DEFAULT_SERVER = config['kafka']['producer']['default-server']
RESULT_TOPIC = config['kafka']['producer']['result-topic']


def get_list_topics():
    admin_client = AdminClient({"bootstrap.servers": ','.join(DEFAULT_SERVER)})
    return admin_client.list_topics().topics


def create_new_topic(topic_name: str):
    admin_client = AdminClient({"bootstrap.servers": ','.join(DEFAULT_SERVER)})
    topic_list = [NewTopic("search_maersk", 1, 1)]
    admin_client.create_topics(topic_list)


def print_consumer_value_from_beginning(topics: list[str] = None):
    conf = {'bootstrap.servers': ','.join(DEFAULT_SERVER),
            'group.id': "foo",
            'enable.auto.commit': False,
            'auto.offset.reset': 'earliest'}

    consumer = Consumer(conf)

    if topics is None:
        topics = RESULT_TOPIC

    try:
        consumer.subscribe(topics)

        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(msg.value())
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()


if __name__ == "__main__":
    # print(get_list_topics())
    print_consumer_value_from_beginning()
