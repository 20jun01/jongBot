from ..model import EventType
from fastapi import Response
from .. import api, const

quiz_posted = False

def event_handler(event: EventType, body: dict) -> Response:
    if event == EventType.PING:
        return Response(status_code=204)
    if event == EventType.MESSAGE_CREATED:
        if not body["message"]["user"]["bot"]:
            message_created_handler(body)
        return Response(status_code=204)

def message_created_handler(body: dict):
    message_sent: str = body["message"]["plainText"]
    channel_id: str = body["message"]["channelId"]
    print(body)
    if message_sent.startswith("@BOT_mahjong"):
        if message_sent.startswith("/leave"):
            api.leave_channel(channel_id)
        if message_sent.startswith("/join"):
            api.join_channel(channel_id)
        if message_sent.startswith("/help"):
            api.post_to_traq(const.get_message("help"), channel_id)
    if message_sent.startswith("/quiz"):
        if quiz_posted:
            api.post_to_traq(const.get_message("quiz_already_posted"), channel_id)
            return
        message = quiz_handler()
        quiz_posted = True
        api.post_to_traq(message, channel_id)
    if message_sent.startswith("/answer"):
        if not quiz_posted:
            api.post_to_traq(const.get_message("quiz_not_posted"), channel_id)
            return
        message_sent.replace("/answer", "").strip()
        message = answer_handler(message_sent)
        quiz_posted = False
        api.post_to_traq(message, channel_id)

def quiz_handler():
    return "test"

def answer_handler(message_sent: str):
    return "test"