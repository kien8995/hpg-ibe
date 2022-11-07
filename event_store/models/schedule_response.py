import json
from types import SimpleNamespace as Namespace


class ScheduleResponse:
    def __init__(self):
        self.type = ""

    @staticmethod
    def of(json_str: str):
        data = json.loads(json_str, object_hook=lambda d: Namespace(**d))

        scheduleResponse = ScheduleResponse()

        return scheduleResponse
