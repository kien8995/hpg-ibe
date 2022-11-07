import json
from types import SimpleNamespace as Namespace

from modules.maersk.response.tracking.container import Container
from modules.maersk.response.tracking.location import Location


class TrackingResponse:
    def __init__(self):
        self.is_container_search = False
        self.containers: list[Container] = []
        self.origin: Location = Location()
        self.destination: Location = Location()

    @staticmethod
    def of(json_str: str):
        data = json.loads(json_str, object_hook=lambda d: Namespace(**d))

        response = TrackingResponse()
        response.is_container_search = data.isContainerSearch

        if hasattr(data, 'containers'):
            for index, val in enumerate(data.containers):
                container = Container.of(val)
                response.containers.append(container)

        response.origin = Location.of(data.origin)
        response.destination = Location.of(data.destination)

        return response

