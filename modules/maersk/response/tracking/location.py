from typing import Any

from modules.maersk.response.tracking.event import Event


class Location:
    def __init__(self):
        self.city = ""
        self.country = ""
        self.country_code = ""
        self.events: list[Event] = []
        self.geo_site = ""
        self.geoid_city = ""
        self.site_type = ""
        self.state = ""
        self.terminal = ""

    @staticmethod
    def of(data: Any):
        location = Location()
        location.city = data.city
        location.country = data.country
        location.country_code = data.country_code

        if hasattr(data, 'events'):
            for index, val in enumerate(data.events):
                location.events.append(Event.of(val))

        location.geo_site = data.geo_site
        location.geoid_city = data.geoid_city
        location.site_type = data.site_type
        location.state = data.state
        location.terminal = data.terminal

        return location
