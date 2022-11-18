import json
from types import SimpleNamespace as Namespace

from event_store.models.base_model import BaseModel


class ScheduleInput(BaseModel):
    def __init__(self):
        super().__init__()
        self.type = ""
        self.dep = ""
        self.arr = ""
        self.date = ""
        self.number_of_weeks = 4

    @staticmethod
    def of(json_str: str):
        data = json.loads(json_str, object_hook=lambda d: Namespace(**d))

        scheduleInput = ScheduleInput()
        scheduleInput.type = data.type
        scheduleInput.dep = data.dep
        scheduleInput.arr = data.arr
        scheduleInput.date = data.date
        if hasattr(data, 'number_of_weeks'):
            scheduleInput.number_of_weeks = data.number_of_weeks

        return scheduleInput
