from kafka import KafkaConsumer
from config import app_config

DEFAULT_SERVER = app_config['kafka']['consumer']['default-server']
CONSUMER_TIMEOUT_MS = app_config['kafka']['consumer']['timeout-ms']
CONSUMER_AUTO_OFFSET_RESET = app_config['kafka']['consumer']['auto-offset-reset']


def get_kafka_consumer(topic_name: str, servers: list[str] = None):
    if servers is None:
        servers = DEFAULT_SERVER

    _consumer = None
    try:
        _consumer = KafkaConsumer(topic_name,
                                  api_version=(0, 10),
                                  bootstrap_servers=servers,
                                  auto_offset_reset=CONSUMER_AUTO_OFFSET_RESET,
                                  consumer_timeout_ms=CONSUMER_TIMEOUT_MS)
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _consumer
