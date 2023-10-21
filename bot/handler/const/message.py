import json
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "message.json")
with open(file_path) as f:
    messages: dict = json.load(f)

def get_message(message_key: str) -> str:
    return messages.get(message_key, "")