"""
    kafka's base message model
"""
import time
import uuid
from datetime import datetime


class BaseMessage:
    """
        base message model class
    """
    def __init__(self):
        self.id = str(uuid.uuid4()).replace('-', '')
        self.epoch_time = int(time.time())
        self.timestamp = datetime.now()
