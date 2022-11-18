from config import setup_logging
from .consumer import get_kafka_consumer
from .producer import get_kafka_producer, publish, publish_message, publish_to_result

setup_logging()
