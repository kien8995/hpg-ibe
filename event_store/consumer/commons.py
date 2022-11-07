from kafka import KafkaConsumer
from config import config

DEFAULT_SERVER = config['kafka']['consumer']['default-server']
CONSUMER_TIMEOUT_MS = config['kafka']['consumer']['timeout-ms']


def get_kafka_consumer(topic_name: str, servers: list[str] = None):
    if servers is None:
        servers = DEFAULT_SERVER

    _consumer = None
    try:
        _consumer = KafkaConsumer(topic_name, auto_offset_reset='earliest', bootstrap_servers=servers,
                                  api_version=(0, 10), consumer_timeout_ms=CONSUMER_TIMEOUT_MS)
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _consumer
