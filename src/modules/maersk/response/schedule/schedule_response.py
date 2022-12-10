"""
    ScheduleResponse response model
"""
import json
from types import SimpleNamespace as Namespace

from modules.maersk.response.schedule.schedule import Schedule


class ScheduleResponse:
    """
        ScheduleResponse model class
    """
    def __init__(self):
        self.product_id = ""
        self.product_sequence = ""
        self.schedules: list[Schedule] = []

    @staticmethod
    def of(json_str: str) -> 'ScheduleResponse':
        """convert json string to ScheduleResponse

        Args:
            json_str (str): json string

        Returns:
            ScheduleResponse: convert result
        """
        data = json.loads(json_str, object_hook=lambda d: Namespace(**d))
        product = data.products[0]

        response = ScheduleResponse()
        response.product_id = product.productId
        response.product_sequence = product.productSequence

        for _, val in enumerate(product.schedules):
            schedule = Schedule.of(val)
            response.schedules.append(schedule)

        return response
