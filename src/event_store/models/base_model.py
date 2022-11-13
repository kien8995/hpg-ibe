from datetime import datetime


class BaseModel:
    def __init__(self):
        self.timestamp = datetime.now()
