from pwn import * # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

for i in range(100):
    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    if received["type"] == "base64":
        base64_bytes = received["encoded"].encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        decoded = message_bytes.decode('ascii')
    elif received["type"] == "hex":
        a_string = bytes.fromhex(received["encoded"])
        decoded = a_string.decode("ascii")
    elif received["type"] == "rot13":
        decoded = codecs.encode(received["encoded"], 'rot_13')
    elif received["type"] == "bigint":
        d = int(received["encoded"],16)
        decoded = (long_to_bytes(d).decode("utf-8"))
        print(decoded)
    elif received["type"] == "utf-8":
        decoded = (''.join([chr(b) for b in received["encoded"]]))

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

json_recv()



'''
        if encoding == "base64":
            encoded = base64.b64encode(self.challenge_words.encode()).decode() # wow so encode
        elif encoding == "hex":
            encoded = self.challenge_words.encode().hex()
        elif encoding == "rot13":
            encoded = codecs.encode(self.challenge_words, 'rot_13')
        elif encoding == "bigint":
            encoded = hex(bytes_to_long(self.challenge_words.encode()))
        elif encoding == "utf-8":
            encoded = [ord(b) for b in self.challenge_words]

'''
