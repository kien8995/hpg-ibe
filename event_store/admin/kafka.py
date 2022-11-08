from confluent_kafka.admin import AdminClient, NewTopic
from config import config

DEFAULT_SERVER = config['kafka']['producer']['default-server']

admin_client = AdminClient({"bootstrap.servers": ','.join(DEFAULT_SERVER)})
print(admin_client.list_topics().topics)

# topic_list = [NewTopic("search_maersk", 1, 1)]
# admin_client.create_topics(topic_list)
