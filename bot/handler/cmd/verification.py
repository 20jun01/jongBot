import os
from fastapi import HTTPException
from ..model import EventType

verificationToken = os.getenv("VERIFICATION_TOKEN")
def verification_handler(headers) -> EventType:
    try:
        event = headers["X-TRAQ-BOT-EVENT"]
        reqID = headers["X-TRAQ-BOT-REQUEST-ID"]
        token = headers["X-TRAQ-BOT-TOKEN"]
    except KeyError:
        raise HTTPException(status_code=403, detail="Forbidden")

    if token != verificationToken:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    try:
        return EventType.value_of(event)
    except ValueError:
        raise HTTPException(status_code=400, detail="Bad Request")