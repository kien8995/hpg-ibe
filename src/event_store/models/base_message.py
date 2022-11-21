import time
import uuid
from datetime import datetime


class BaseMessage:
    def __init__(self):
        self.id = str(uuid.uuid4()).replace('-', '')
        self.epoch_time = int(time.time())
        self.timestamp = datetime.now()
