import argparse
import socket
import sys
from functools import partial
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import generate_private_key
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
import keyboard

DEFAULT_PUBLIC_EXPONENT = 65537
HASH_ALGO = hashes.SHA256()
PADDING = padding.OAEP(
    mgf=padding.MGF1(HASH_ALGO),
    algorithm=HASH_ALGO,
    label=None
)

def encrypt_message(message: str, public_key=None) -> bytes:
    """Encrypts the given text using the provided public key."""
    if public_key is None:
        return message
    return public_key.encrypt(message, PADDING)

def decrypt_message(encrypted_message: bytes, private_key=None) -> str:
    """Decrypts the given encrypted text using the provided private key."""
    if private_key is None:
        return encrypted_message
    return private_key.decrypt(encrypted_message, PADDING)

def serialize_key_event(key_event: keyboard.KeyboardEvent) -> bytes:
    """
    (2 Marks)
    Serializes a key event into a format suitable for network transmision.
    The formatted key event should be in the format expected by the
    associated parse_formatted_key_event function.
    """
    return f"{key_event.event_type}--{key_event.scan_code}--{key_event.name}".encode("utf-8")

def deserialize_formatted_key_event(serialized_key_event: bytes) -> keyboard.KeyboardEvent:
    """
    (2 Marks)
    Parses a serialized key event into a keyboard.KeyboardEvent.
    """
    event_type, scan_code, name = serialized_key_event.decode("utf-8").split("--")
    return keyboard.KeyboardEvent(event_type, int(scan_code), name)

def transmit_keyevent(conn: socket.socket, key_event: keyboard.KeyboardEvent, public_key=None):
    """
    (2 Marks)
    This function should simply serialize the provided key event using the
    serialize_key_event function, and send it via the provided socket connection -
    optionally encrypting using the publick key.
    """
    conn.sendall(encrypt_message(serialize_key_event(key_event), public_key))

def should_transmit_keyevent(key_event: keyboard.KeyboardEvent, transmitted_down_keys: set):
    """
    (4 Marks)
    This function determines if a key event should be transmitted. A down
    keypress for a particular key should only be transmitted **once** for
    the duration of the time the key is held down. The `transmitted_down_keys` parameter
    of this function is a set (https://docs.python.org/3/library/stdtypes.html#set)
    containing the name of all the keys which:
        1. Are currently being held down
        2. Have already transmitted an associated down key event
    You should use this set as part of your implementation of this function.
    """
    if key_event.event_type == "down" and key_event.name in transmitted_down_keys:
        return False
    return True

def handle_keyevent(conn: socket.socket, transmitted_down_keys: set, key_event: keyboard.KeyboardEvent, public_key=None):
    """
    (5 Marks)
    This function will be invoked whenever a key event is raised by the keyboard module.
    In this function you should do the following:
        1. Use the should_transmit_keyevent function above to determine if you should
           transmit the given key_event. If the function returns True, then you should
           transmit the frame using the transmit_keyevent function.
        2. If you transmit a DOWN key event - then you should add that key to the
           transmitted_down_keys set which is passed into this function.
        3. If it is an UP key event then you should remove the released key from
           the transmitted_down_keys set.
    """
    if not should_transmit_keyevent(key_event, transmitted_down_keys):
        return
    if key_event.event_type == "down":
        transmitted_down_keys.add(key_event.name)
    elif key_event.event_type == "up" and key_event.name in transmitted_down_keys:
        transmitted_down_keys.remove(key_event.name)
    transmit_keyevent(conn, key_event, public_key=public_key)

def start_server(host, port, public_key):
    """
    (10 Marks)
    This function should open an (AF_INET, SOCK_STREAM) socket and bind it
    to the provided (host, port). It should then start listening and then accept
    a single connection. Once the first connection is established it should
    use the following code snippet to respond to keypresses:

    keyboard.hook(partial(handle_keyevent, conn, set()))
    keyboard.wait()
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen()
        conn, _ = sock.accept()
        with conn:
            keyboard.hook(partial(handle_keyevent, conn, set(), public_key=public_key))
            keyboard.wait()

def replay_key_event(key_event: keyboard.KeyboardEvent):
    """
    Replays the given 
    """
    try:
        if key_event.event_type == "down":
            keyboard.press(key_event.name)
        elif key_event.event_type == "up":
            keyboard.release(key_event.name)
    except ValueError as error:
        print(f"Fail to replay key event: {error}", file=sys.stderr)

def handle_recieved_serialized_key_event(serialized_key_event: bytes, private_key=None):
    """
    This function is called whenever the client recieves a formatted key event.
    Remember that the formatted key event *may* have been encrypted and thus
    require decryption using the private key.

    You should use this function to replay the keyevent.
    """
    replay_key_event(deserialize_formatted_key_event(decrypt_message(serialized_key_event, private_key)))

def start_client(host, port, private_key):
    """
    (10 Marks)
    This function should open an (AF_INET, SOCK_STREAM) socket and connect
    to the provided (host, port). It should continuously wait to recieve (using recv())
    any key event messages from the server. It should then parse the key event
    message and replay it using the keyboard module's press() and release()
    functions.

    Look at the example echo server's code:

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        ...
        with conn:
            ...
            while True:
                data = str(conn.recv(1024), "utf-8")
                if not data:
                    break
                ...

    In particular how it uses the recv() method, and if that method returned
    an empty string (aka not data would be True) then it stops the loop.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        n_msg_bytes = private_key.key_size // 8 if private_key is not None else 1024
        while True:
            serialized_key_event = sock.recv(n_msg_bytes)
            print(serialized_key_event)
            handle_recieved_serialized_key_event(serialized_key_event, private_key=private_key)

def get_argument_parser():
    parser = argparse.ArgumentParser("Remote Keyboard")
    subparsers = parser.add_subparsers(dest="mode")
    client_parser = subparsers.add_parser("client", help="Client Mode")
    client_parser.add_argument("--host", type=str, required=True, help="The IP address of the host to conenct to.")
    client_parser.add_argument("--port", type=int, required=True, help="The port to conenct to.")
    client_parser.add_argument("--private-key", type=argparse.FileType("rb"), help="The private key with which to decrypt data sent from the server.")
    client_parser.add_argument("--passphrase", type=bytes, help="The passphrase for the private key.")
    server_parser = subparsers.add_parser("server", help="Server Mode")
    server_parser.add_argument("--host", type=str, required=False, default="", help="The IP address of the interface to listen on.")
    server_parser.add_argument("--port", type=int, required=True, help="The port to listen on.")
    server_parser.add_argument("--public-key", type=argparse.FileType("rb"), help="The public key with which to encrypt data which is sent to the client.")
    keygen_parser = subparsers.add_parser("keygen", help="Generate PGP Keys")
    keygen_parser.add_argument("--public-key", type=argparse.FileType("wb+"), required=True, help="The file to write the public key to.")
    keygen_parser.add_argument("--private-key", type=argparse.FileType("wb+"), required=True, help="The file to write the private key to.")
    keygen_parser.add_argument("--key-size", type=int, default=2048, choices=[1024, 2048, 4096, 8192], help="The size of the key to generate.")
    keygen_parser.add_argument("--passphrase", type=bytes, help="The passphrase for the private key.")
    return parser

def main(argv = None):
    argv = argv or sys.argv[1:]
    parser = get_argument_parser()
    result = parser.parse_args(argv)
    if result.mode == "server":
        public_key = load_pem_public_key(result.public_key.read()) if result.public_key else None
        start_server(result.host, result.port, public_key)
    elif result.mode == "client":
        private_key = load_pem_private_key(result.private_key.read(), password=result.passphrase) if result.private_key else None
        start_client(result.host, result.port, private_key)
    elif result.mode == "keygen":
        private_key = generate_private_key(public_exponent=DEFAULT_PUBLIC_EXPONENT, key_size=result.key_size)
        public_key = private_key.public_key()
        result.private_key.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(result.passphrase) if result.passphrase else serialization.NoEncryption()
        ))
        result.public_key.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.PKCS1
        ))

if __name__ == "__main__":
    main()
