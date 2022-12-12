"""
    schedule input model
"""
import json
from types import SimpleNamespace as Namespace

from event_store.models.base_message import BaseMessage


class ScheduleInput(BaseMessage):
    """
        ScheduleInput model class
    """
    def __init__(self):
        super().__init__()
        self.type = ""
        self.dep = ""
        self.arr = ""
        self.date = ""
        self.dep_id = ""
        self.arr_id = ""
        self.number_of_weeks = 4

    @staticmethod
    def of(json_str: str) -> 'ScheduleInput':
        """convert json string to ScheduleInput

        Args:
            json_str (str): json string

        Returns:
            ScheduleInput: convert result
        """
        data = json.loads(json_str, object_hook=lambda d: Namespace(**d))

        schedule_input = ScheduleInput()
        schedule_input.type = data.type
        schedule_input.dep = data.dep
        schedule_input.arr = data.arr
        schedule_input.date = data.date
        if hasattr(data, 'dep_id'):
            schedule_input.dep_id = data.dep_id
        if hasattr(data, 'arr_id'):
            schedule_input.arr_id = data.arr_id
        if hasattr(data, 'number_of_weeks'):
            schedule_input.number_of_weeks = data.number_of_weeks

        return schedule_input
