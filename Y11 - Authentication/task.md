# Encryption and Authentication

## Task 1 - Hashing Files

Use the `main.py` file to determine which file in the `/files` directory corressponds to each row in the table found below by using the `hash` command.

```sh
$ main.py hash --file server.py --algo sha1
71a4a657d7f32db8eaae3160c50a027850b1a330
```


|Algorithim|Hash|File (TODO)|
|---|---|---------|
|MD5|0cc175b9c0f1b6a831c399e269772661||
|SHA256|ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb||
|SHA1|84a516841ba77a5b4648de2cd0dfcb30ea46dbb4||
|SHA1|3c363836cf4e16666669a25da280a1865c2d2874||

## Task 2 - Real World Usecase

Research and then describe (in detail - 2/3 paragraphs) *how* and *why* hash functions are used in either of the two following scenarios:
1. Storing secrets in a database (e.g. passwords).
2. Ensuring you have downloaded the correct version of a file (e.g. https://www.getmonero.org/downloads/ has a "Verify" section)

## Task 3 - Have a Chat

Use the `main.py` file to have a chat with a few of your peers! At this stage don't worry about signing your messages! Ensure ALL group members connect to the _Network Wall_ LAN so one member can run the server using `server.py` and the others can connect to it easily.

### Running The Server

```sh
$ ./server.py --port 50008
Bottle v0.13-dev server starting up (using WSGIRefServer())...
Listening on http://127.0.0.1:50008/
Hit Ctrl-C to quit.
```
### Saying Something

```sh
$ ./main.py say --host 127.0.0.1 --port 50008 --username server --message "hello world"             
[1] server said "hello world" 
```

### Hear Messages

```sh
$ ./main.py hear --host 127.0.0.1 --port 50008
[0] server said "hello world" 
[1] server said "hello world" 
[2] bob said "no i am!"
```

## Task 4 - Rolodex

You'll notice a `rolodex.json` file which initially contains the following JSON:

```json
{
    "henry": "./keys/henry.pub",
    "server": "./keys/server.pub"
}
```

This rolodex file is YOUR PERSPECTIVE on which public key (remember this corresponds to a private key!) is associated with a given username. You and all of your friends should generate your own **key pair** with the following command (replace `<username>` with your username!):

```sh
$ ./main.py keygen --public-key ./keys/<username>.pub --private-key ./keys/<username>
```

You should then send the `<username>.pub` ***public key*** to your friends, and they should copy it into the `/keys` directory and add another association to the `rolodex.json` file.

## Task 5 - Authenticated Messaging

Now that everyone has generated their own public/private keypair, and added their friends to their rolodex you should have a go at sending **authenticated** messages using the following command (again, replace `<username>` with YOUR username - ensure the private key file exists at that location!):

```sh
$ ./main.py say --host 127.0.0.1 --port 50008 --username <username> --private-key ./keys/<username> --message "..."
$ ./main.py hear --host 127.0.0.1 --port 50008
[0] server said "hello world"
[2] bob said "no i am!"
[4] server said "i am there server" (7652096328...)
[5] henry said "i am there server" (5ff4dbcf5c...)
```

Experiment with sending messages as people you aren't, with different private keys, and no private keys at all - take note of the differnet colors of text which are displayed.

Answer the following questions:

1. What does a **yellow** username mean?
2. What does it mean if there is no signature (e.g. `(765fc...)`)?
3. What does a **green** signature mean?

## Task 6 - Encrypted Messaging

Our messages are transmited in plain text! Anyone connected to your server can see all of your messages... even if they aren't in your rolodex or your friend! We should probably fix that...

Use the following webpage https://cryptography.io/en/latest/fernet/ to implement *symmetric encryption* of the **message**. This will require you to do the following:

1. In `server.py` have the server also accept & record a hash of the secret (if any) in each message tuple of `MESSAGES` indicating if the message contents are encrypted.
2. Adjust the `say` function in `main.py` to take an *optional* `secret` parameter, if the parameter `is not None` then you should hash it and add it to the `form` dictionary.
3. Adjust the `hear` function in `main.py` to take an *optional* `secret` parameter, if the parameter `is not None` then when printing out each message, check if the message's secret hash matches the `secret` parameter - if it does then use the secret to decrypt the message! If a message is encrypted, but you don't know the secret to decrypt it then display a 🔒 (lock) emoji after the signature, if you decrypted the message display a 🔓 (unlocked) emoji. If a message is unencrypted don't do anything different.
