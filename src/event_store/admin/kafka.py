import sys

from confluent_kafka import Consumer, KafkaException, KafkaError
from confluent_kafka.admin import AdminClient, NewTopic
from config import app_config

DEFAULT_SERVER = app_config['kafka']['producer']['default-server']
RESULT_TOPIC = app_config['kafka']['producer']['result-topic']


def get_list_topics(admin_client: AdminClient):
    return admin_client.list_topics().topics


def create_new_topic(admin_client: AdminClient, topic_name: str):
    topic_list = [NewTopic(topic_name, 1, 1)]
    admin_client.create_topics(topic_list)


def create_new_topics(admin_client: AdminClient, topic_names: list[str]):
    topic_list = []
    for index, val in enumerate(topic_names):
        topic_list.append(NewTopic(val, 1, 1))
    admin_client.create_topics(topic_list)


def delete_topics(admin_client: AdminClient, topic_names: list[str]):
    fs = admin_client.delete_topics(topic_names, operation_timeout=30)

    # Wait for operation to finish.
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print("Topic {} deleted".format(topic))
        except Exception as e:
            print("Failed to delete topic {}: {}".format(topic, e))


def print_consumer_value(consumer: Consumer, topics: list[str] = None):
    if topics is None:
        topics = [RESULT_TOPIC]

    try:
        consumer.subscribe(topics)

        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue

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
    # admin_client = AdminClient({"bootstrap.servers": ','.join(DEFAULT_SERVER)})
    # print(get_list_topics(admin_client))

    conf = {'bootstrap.servers': ','.join(DEFAULT_SERVER),
            'group.id': "foo",
            'enable.auto.commit': False,
            'auto.offset.reset': 'earliest'}
    consumer = Consumer(conf)

    print_consumer_value(consumer)
