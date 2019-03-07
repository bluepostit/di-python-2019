import json


MESSAGE_FILE_PATH = 'data/messages.json'


def get_all_messages():
    messages = []
    with open(MESSAGE_FILE_PATH) as f:
        messages = json.load(f)
    return messages


def save_messages(messages):
    with open(MESSAGE_FILE_PATH, 'w') as f:
        json.dump(messages, f)


def get_messages(username):
    messages = [message for message in get_all_messages() if message['to'] == username]
    return messages


def get_message(id):
    for message in get_all_messages():
        if message['id'] == id:
            return message
    else:
        return None


def get_max_id(messages):
    max_id = 0
    for message in messages:
        if message['id'] > max_id:
            max_id = message['id']
    return max_id


def add(message):
    messages = get_all_messages()
    id = get_max_id(messages) + 1
    message['id'] = id
    messages.append(message)
    save_messages(messages)