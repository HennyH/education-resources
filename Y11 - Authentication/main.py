#!/usr/bin/env python3
import argparse
import json
from inspect import isclass
from os import urandom
from re import sub
from server import say
from typing import Optional, Tuple
from urllib.request import urlopen
from urllib.parse import urlencode
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, utils
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import generate_private_key
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.exceptions import InvalidSignature
from color import green, yellow, red, bold, underline, italic

DEFAULT_PUBLIC_EXPONENT = 65537
SIGNATURE_HASH_ALGO = hashes.SHA256
HASH_ALGOS = [hashes.SHA256, hashes.MD5, hashes.SHA1]
HASH_ALGO_NAME_TO_CLS_NAME = {hc.name: hc.__name__ for hc in HASH_ALGOS}

def get_hash(data: bytes, algo_name: str) -> bytes:
    if algo_name not in HASH_ALGO_NAME_TO_CLS_NAME:
        raise ValueError(f"The hashing algorithim {algo_name} was not found.")
    algo: hashes.HashAlgorithm = getattr(hashes, HASH_ALGO_NAME_TO_CLS_NAME[algo_name])
    digest = hashes.Hash(algorithm=algo())
    digest.update(data)
    return digest.finalize()

def generate_asym_keypair(key_size: int, passphrase: Optional[str]) -> Tuple[bytes, bytes]:
    private_key = generate_private_key(public_exponent=DEFAULT_PUBLIC_EXPONENT, key_size=key_size)
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(passphrase) if passphrase else serialization.NoEncryption()
    )
    public_key = private_key.public_key()
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1
    )
    return (private_key_bytes, public_key_bytes)

def format_message(message, rolodex):
    mid, user, message, signature = message
    # prepare the username text
    user_text = user
    if signature is None:
        user_text = red(user_text)
    if user in rolodex:
        user_text = bold(user_text)
    else:
        user_text = underline(user_text)
    # prepare the sig text
    sig_text = ""
    if signature is not None:
        sig_text = f"({signature[:10]}...)"
        sig_bytes = bytes.fromhex(signature)
        if user not in rolodex:
            sig_text = red(sig_text)
        else:
            public_key = rolodex[user]
            hasher = hashes.Hash(SIGNATURE_HASH_ALGO())
            hasher.update(message.encode("utf-8"))
            digest = hasher.finalize()
            try:
                public_key.verify(
                    sig_bytes,
                    digest,
                    padding.PSS(
                        mgf=padding.MGF1(SIGNATURE_HASH_ALGO()),
                        salt_length=padding.PSS.MAX_LENGTH),
                    utils.Prehashed(SIGNATURE_HASH_ALGO())
                )
                sig_text = green(sig_text)
            except InvalidSignature:
                sig_text = underline(red(sig_text))
                user_text = yellow(user_text)
    return f"[{mid}] {user_text} {italic('said')} \"{message}\" {sig_text}"

def say(host: str, port: int, message: str, username: str, private_key, rolodex) -> None:
    form = {"username": username, "message": message}
    if private_key is not None:
        hasher = hashes.Hash(SIGNATURE_HASH_ALGO())
        hasher.update(message.encode("utf-8"))
        digest = hasher.finalize()
        form["signature"] = private_key.sign(
            digest,
            padding.PSS(
                mgf=padding.MGF1(SIGNATURE_HASH_ALGO()),
                salt_length=padding.PSS.MAX_LENGTH),
            utils.Prehashed(SIGNATURE_HASH_ALGO())
        ).hex()
    data = urlencode(form).encode("ascii")
    with urlopen(f"http://{host}:{port}/say", data) as response:
        message_json = response.read().decode("utf-8")
        message = json.loads(message_json)
        print(format_message(message, rolodex))

def hear(host, port, msg_id, after_id, before_id, rolodex):
    params = {}
    if msg_id is not None:
        params["id"] = msg_id
    if after_id is not None:
        params["after"] = after_id
    if before_id is not None:
        params["before"] = before_id
    with urlopen(f"http://{host}:{port}/hear?{urlencode(params)}") as response:
        data = response.read().decode("utf-8")
        messages = json.loads(data)
    for message in messages:
        print(format_message(message, rolodex))

def load_rolodex(rolodex_filename):
    rolodex = {}
    with open(rolodex_filename, "r") as rolodex_fileobj:
        for username, pub_key_filename in json.load(rolodex_fileobj).items():
            try:
                with open(pub_key_filename, "rb") as pub_key_fileobj:
                    rolodex[username] = load_pem_public_key(pub_key_fileobj.read())
            except Exception as error:
                print(f"Failed to load rolodex user {username}'s public key file {pub_key_filename}: {error}")
    return rolodex

if __name__ == "__main__":
    parser = argparse.ArgumentParser("AuthTool")
    subparsers = parser.add_subparsers(dest="mode")
    hash_parser = subparsers.add_parser("hash")
    hash_parser.add_argument("--file", type=argparse.FileType("rb"), required=True, help="The filename of the file whose contents should be hashed.")
    hash_parser.add_argument("--algo", type=str, choices=HASH_ALGO_NAME_TO_CLS_NAME.keys(), required=True, help="The hash algorithim whith which to hash the file.")
    keygen_parser = subparsers.add_parser("keygen", help="Generate PGP Keys")
    keygen_parser.add_argument("--public-key", type=argparse.FileType("wb+"), required=True, help="The file to write the public key to.")
    keygen_parser.add_argument("--private-key", type=argparse.FileType("wb+"), required=True, help="The file to write the private key to.")
    keygen_parser.add_argument("--key-size", type=int, default=2048, choices=[1024, 2048, 4096, 8192], help="The size of the key to generate.")
    keygen_parser.add_argument("--passphrase", type=bytes, help="The passphrase for the private key.")
    say_parser = subparsers.add_parser("say")
    say_parser.add_argument("--host", type=str, required=True, help="The message server to send the message to.")
    say_parser.add_argument("--port", type=int, required=True, help="The port of the message server to send the message to.")
    say_parser.add_argument("--username", type=str, required=True, help="The username to send the message under.")
    say_parser.add_argument("--private-key", type=argparse.FileType("rb"), help="The private key to sign the message with.")
    say_parser.add_argument("--passphrase", type=str, help="The private key to sign the message with.")
    say_parser.add_argument("--message", type=str, required=True, help="The text of the message to send.")
    say_parser.add_argument("--rolodex", type=load_rolodex, default="./rolodex.json", help="The json file containing a mapping from usernames to public keys.")
    hear_parser = subparsers.add_parser("hear")
    hear_parser.add_argument("--host", type=str, required=True, help="The message server host to hear messages from.")
    hear_parser.add_argument("--port", type=int, required=True, help="The port of the message server to hear messages from.")
    hear_parser.add_argument("--msg-id", type=int, help="Retrieves a specific message with the given id.")
    hear_parser.add_argument("--after-id", type=int, help="Retrieves messages which occur after the given id.")
    hear_parser.add_argument("--before-id", type=int, help="Retrieves messages which occur before the given id.")
    hear_parser.add_argument("--rolodex", type=load_rolodex, default="./rolodex.json", help="The json file containing a mapping from usernames to public keys.")
    result = parser.parse_args()
    if result.mode == "hash":
        digest = get_hash(result.file.read(), result.algo)
        print(digest.hex())
    elif result.mode == "keygen":
        private_key_bytes, public_key_bytes = generate_asym_keypair(result.key_size, result.passphrase)
        result.private_key.write(private_key_bytes)
        result.public_key.write(public_key_bytes)
    elif result.mode == "say":
        private_key = load_pem_private_key(result.private_key.read(), result.passphrase) if result.private_key else None
        say(result.host, result.port, result.message, result.username, private_key, result.rolodex)
    elif result.mode == "hear":
        hear(result.host, result.port, result.msg_id, result.after_id, result.before_id, result.rolodex)

