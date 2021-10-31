from Crypto.PublicKey import RSA
from base64 import b64decode
f = open("/home/kali/Downloads/transparency_afff0345c6f99bf80eab5895458d8eab.pem",'r')
key = f.read()
print(key)
print(RSA.importKey(key).d)
