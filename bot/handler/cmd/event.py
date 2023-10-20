from ..model import EventType
from fastapi import Response

def event_handler(event: EventType) -> Response:
    if event == EventType.PING:
        return Response(status_code=204)