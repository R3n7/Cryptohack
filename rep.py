#nc ctf.hackucf.org 10101
from pwn import * # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import long_to_bytes

r = remote('ctf.hackucf.org', 10101)

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

for i in range(100):
    received = json_recv()

    print("Received type: ")
    print(received)
    '''to_send = {
        "decoded": decoded
    }
    json_send(to_send)

json_recv()'''