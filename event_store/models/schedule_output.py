import json
from types import SimpleNamespace as Namespace


class ScheduleOutput:
    def __init__(self):
        self.type = ""

    @staticmethod
    def of(json_str: str):
        data = json.loads(json_str, object_hook=lambda d: Namespace(**d))

        scheduleResponse = ScheduleOutput()

        return scheduleResponse
