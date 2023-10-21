from ..model import EventType, convert_to_message, convert_chinitsu_str_to_message, TileType
from fastapi import Response
from .. import api, const
from .mahjong import chinitsu_agari_check, chinitsu_tehai_generator

quiz_posted = False
quiz_tehai = ""
agarihais = ""

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
        return
    if message_sent.startswith("/quiz"):
        if quiz_posted:
            api.post_to_traq(const.get_message("quiz_already_posted"), channel_id)
            return
        message = quiz_handler()
        prefix = const.get_message("quiz")
        quiz_posted = True
        api.post_to_traq(prefix + message, channel_id)
        return
    if message_sent.startswith("/answer"):
        if not quiz_posted:
            api.post_to_traq(const.get_message("quiz_not_posted"), channel_id)
            return
        message_sent.replace("/answer", "").strip()
        is_agari = answer_handler(message_sent)
        message = const.get_message("correct") if is_agari else const.get_message("incorrect")
        api.post_to_traq(message, channel_id)
        return
    if message_sent.startswith("/stop"):
        quiz_posted = False
        message = stop_handler()
        string_with_format = const.get_message("stop")
        message = string_with_format.format(message)
        api.post_to_traq(message, channel_id)
        return

def quiz_handler():
    global quiz_tehai, agarihais
    tehai = chinitsu_tehai_generator()
    quiz_tehai = tehai
    message = convert_chinitsu_str_to_message(tehai)

    agarihais = ""
    for i in range(1, 10):
        if chinitsu_agari_check(quiz_tehai + str(i)):
            agarihais = str(i)
    return message

def answer_handler(message_sent: str) -> bool:
    return agarihais == message_sent

def stop_handler():
    return convert_chinitsu_str_to_message(agarihais)