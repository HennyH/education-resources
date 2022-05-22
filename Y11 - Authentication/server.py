#!/usr/bin/env python3
import argparse
import json
from threading import Lock
from bottle import post, get, abort, run, request, response

MESSAGES_MUTEX = Lock()
MESSAGES = [
    # (id, username, message, signature?)
    (0, "server", "hello world", None)
]

@post("/say")
def say():
    username = request.forms.get("username")
    if not username:
        abort(code=400, text="username required")
    message = request.forms.get("message")
    if not message:
        abort(code=400, text="message expected")
    signature = request.forms.get("signature")
    response.add_header("Content-Type", "application/json")
    MESSAGES_MUTEX.acquire()
    try:
        MESSAGES.append((len(MESSAGES), username, message, signature))
        return json.dumps(MESSAGES[-1])
    finally:
        MESSAGES_MUTEX.release()

@get("/hear")
def hear():
    msg_id = request.query.id or None
    after_id = request.query.after or None
    before_id = request.query.before or None
    matching_messages = MESSAGES
    if msg_id is not None:
        msg_id = int(msg_id)
        matching_messages = [msg for msg in matching_messages if msg[0] == msg_id]
    if after_id is not None:
        after_id = int(after_id)
        matching_messages = [msg for msg in matching_messages if msg[0] > after_id]
    if before_id is not None:
        before_id = int(before_id)
        matching_messages = [msg for msg in matching_messages if msg[0] < before_id]
    response.add_header("Content-Type", "application/json")
    return json.dumps(matching_messages)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Chat Server")
    parser.add_argument("-p", "--port", type=int, required=False, default=50008)
    result = parser.parse_args()
    run(port=result.port)
