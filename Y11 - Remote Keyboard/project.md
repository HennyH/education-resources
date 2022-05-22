# Remote Keyboard - Part 1

## Learning Objectives

- To be able to develop simple programs which use TCP.
    - "Technologies appropriate for the implementation of a client/server and peer-to-peer network"
- Understand the security implications of non-authenticated, non-signed and non-encrypted communication.
- Know how to authenticate, sign and encrypt a message.

## Background

During the past year many people have been confined to their homes as part of COVID lockdowns. This made it very difficult to play local 2 player co-op games with a friend. You and your friend particularly enjoy playing the game Fireboy and Watergirl (https://www.fireboynwatergirl.com/). Being a knowledge computer science student you decide to create a program which will allow you to play the game together across the internet!

## Your Solution

You decide to write a program to transmit and replay keystrokes over a TCP connection. Your program can run in one of two modes: client mode or server mode. In server mode you listen for keystrokes (keydown and keyup) on your keyboard, and then transmit them to the connected client. In client mode you connect to a server and recieve a sequence of keydown or keyup messages.

```
+------------+              +-------------+                      
|            |              |             |                      
|            |     TCP      |             |                      
|   Server   --------------->   Client    |                      
|            |              |             |                      
|            |              |             |                      
+------↑-----+              +------|------+                      
       |                           |                             
       | Server Keystroke          | Server Keystroke            
       |                           |                             
+------|------+            +-------↓------+                      
|  Keyboard   |            |  Keyboard    |                      
+-------------+            +-------|------+                      
                                   |                             
                                   | Server & Client Keystroke   
                                   |                             
                          +--------↓--------+                    
                          |      Game       |                    
                          +-----------------+
```

### Requirements

In order to produce your program you should make use of the following modules:

#### keyboard (0.13.5)

The keyboard module (https://pypi.org/project/keyboard/) makes it easy to listen for keystrokes and replay them. This is an **external** module, and thus you will need to install it on your system. This can be done by executing either of the following commands from a terminal:

```shell
$ pip install keyboard
OR
$ python -m pip install keyboard
```

If your system complains that there is no such program or module `pip`, then you will need to install it. This is quite simple but also platform specific - use google!

The documentation for this module is available on it's GitHub page which is located at the following url: https://github.com/boppreh/keyboard

In particular you should pay attention to the "Common patterns and mistakes" section (https://github.com/boppreh/keyboard#common-patterns-and-mistakes).

#### socket

This is the built-in standard python library for doing networking. It makes it easy to use TCP to create a client/server program. The **Example** section of the documentation page (https://docs.python.org/3/library/socket.html#example) explains how to build a simple echo server. The code for which has been copied below for your convenience.

```py
# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = str(conn.recv(1024), "utf-8")
            if not data:
                break
            conn.sendall(data)
```

```py
# Echo client program
import socket

HOST = 'daring.cwi.nl'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall('Hello, world'.encode("utf-8"))
    data = s.recv(1024)
print('Received', repr(data))
```

## Tasks (/65 Marks)

### TCP (25 Marks)

Answer the following questions:

1. (2 Marks) Define TCP in one or two sentences.
2. (3 Marks) Describe the relationship between TCP and IP in one or two sentences.
3. (10 Marks) State whether TCP or UDP is the more appropriate transport protocol for this application - justify your answer with reference to the characteristics of both protocols. You answer should be sufficently detailed (5 - 7 well reasoned sentences) to attain full marks.
4. (10 Marks) Based upon the local area network setup illustrated below, describe the 'journey' of a transmitted key event from the server to the client (exclude the TCP handsake and acknowledgement of delivery). In particular discuss the following points:
    - Encapsulation of TCP data into an IP datagram.
    - Encapsulation of an IP datagram within an Ethernet frame/packet.
    - Retransmissions of Ethernet packets, including the changes in the source MAC address.
    - The server's reading of the Etherent packet's headers and payload, in particular how it determines if it is the intended recipient of the packet and the embedded datagram.

```
                  +------------+                  
+--------+  Eth   |            |  Eth   +--------+
| Client ----------    Hub     ---------- Server |
+--------+        |            |        +--------+
                  +------------+                 
```

### Implementation (35 Marks)

You must implement the following function in the `main.py` python file:

- (2 Marks) `format_key_event`.
- (2 Marks) `parse_formatted_key_event`.
- (2 Marks) `transmit_keyevent`.
- (4 Marks) `should_transmit_keyevent`.
- (5 Marks) `handle_keyevent`.
- (10 Marks) `start_server`.
- (10 Marks) `start_client`.

If your function's implementation is correct (that is, it correctly satisfies the
requirements stated within the docstrings) then you will be awarded full points.

If you solution is not correct then for each line which requires fixing either 1 or 2 marks will be deducted based upon the size of the change.

### Style (5 Marks)

The 5 marks for style are awarded based upon the simplicity, elegance, readabiltiy and pythonic-ness of your implementation.

## Code Template

```
import argparse
import socket
import sys
from functools import partial
import keyboard

def format_key_event(key_event):
    """
    (2 Marks)
    Formats a key event into a format suitable for network transmision.
    The formatted key event should be in the format expected by the
    associated parse_formatted_key_event function.

    Remember:

    - key_event.event_type gives you back the type of event ("up" or "down")
    - key_event.name gives you the key that was pressed ("A", "W", etc...)
    """
    pass

def parse_formatted_key_event(formatted_key_event):
    """
    (2 Marks)
    Parses a formatted key event into a tuple containing the type of the
    event ("up" or "down") and they key involved (e.g. "W", "A", etc...).

    You may not have used a tuple before... You can read more about them
    here: https://docs.python.org/3/library/stdtypes.html#tuple
    """
    pass

def transmit_keyevent(conn: socket.socket, key_event):
    """
    (2 Marks)
    This function should simply format the provided key event using the
    format_key_event function, and send it via the provided socket connection.
    """
    pass

def should_transmit_keyevent(key_event, transmitted_down_keys: set):
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
    
    Remember:

    - key_event.event_type gives you back the type of event ("up" or "down")
    - key_event.name gives you the key that was pressed ("A", "W", etc...)
    """
    pass

def handle_keyevent(conn: socket.socket, transmitted_down_keys: set, key_event):
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

    Remember:

    - key_event.event_type gives you back the type of event ("up" or "down")
    - key_event.name gives you the key that was pressed ("A", "W", etc...)
    """
    pass
            
def start_server(host, port):
    """
    (10 Marks)
    This function should open an (AF_INET, SOCK_STREAM) socket and bind it
    to the provided (host, port). It should then start listening and then accept
    a single connection. Once the first connection is established it should
    use the following code snippet to respond to keypresses:

    keyboard.hook(partial(handle_keyevent, conn, set()))
    keyboard.wait()
    """
    pass

def start_client(host, port):
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
    pass

def get_argument_parser():
    parser = argparse.ArgumentParser("Remote Keyboard")
    subparsers = parser.add_subparsers(dest="mode")
    client_parser = subparsers.add_parser("client", help="Client Mode")
    client_parser.add_argument("--host", type=str, required=True, help="The IP address of the host to conenct to.")
    client_parser.add_argument("--port", type=int, required=True, help="The port to conenct to.")
    server_parser = subparsers.add_parser("server", help="Server Mode")
    server_parser.add_argument("--host", type=str, required=False, default="", help="The IP address of the interface to listen on.")
    server_parser.add_argument("--port", type=int, required=True, help="The port to listen on.")
    return parser

def main(argv = None):
    argv = argv or sys.argv[1:]
    parser = get_argument_parser()
    result = parser.parse_args(argv)
    if result.mode == "server":
        start_server(result.host, result.port)
    elif result.mode == "client":
        start_client(result.host, result.port)

if __name__ == "__main__":
    main()
```

# Remote Keyboard - Part 2

## Security Questions

- Should we allow the client/server to restrict which key strokes it will replay?
- How do we know that our friend is the one who actually connected to our computer? What are the security implications of this?
- Could a hacker launch a man-in-the-middle attack and change our transmitted keystrokes before they get to the client? What are the security implications of this?
- Is running this program tantamount to running a keylogger?