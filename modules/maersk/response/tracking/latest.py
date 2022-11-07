from typing import Any


class Latest:
    def __init__(self):
        self.actfor = ""
        self.activity = ""
        self.actual_time = ""
        self.city = ""
        self.country = ""
        self.country_code = ""
        self.geo_site = ""
        self.state = ""
        self.stempty = False

    @staticmethod
    def of(data: Any):
        event = Latest()
        event.actfor = data.actfor
        event.activity = data.activity
        event.actual_time = data.actual_time
        event.city = data.city
        event.country = data.country
        event.country_code = data.country_code
        event.geo_site = data.geo_site
        event.state = data.state
        event.stempty = data.stempty

        return event

