import json
from types import SimpleNamespace as Namespace


class ScheduleInput:
    def __init__(self):
        self.type = ""
        self.dep = ""
        self.arr = ""
        self.date = ""

    @staticmethod
    def of(json_str: str):
        data = json.loads(json_str, object_hook=lambda d: Namespace(**d))

        scheduleInput = ScheduleInput()
        scheduleInput.type = data.type
        scheduleInput.dep = data.dep
        scheduleInput.arr = data.arr
        scheduleInput.date = data.date

        return scheduleInput
