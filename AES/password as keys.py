import requests
import hashlib
from Crypto.Cipher import AES
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return decrypted.hex()
with open("words") as f:
    words = [w.strip() for w in f.readlines()]
for i in words:
    ciphertext = 'c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66'
    
    KEY = hashlib.md5(i.encode()).digest().hex()
    plaintext = decrypt(ciphertext,KEY)
    try:
        print("flag", bytearray.fromhex(plaintext).decode())
        print(i)
        print(KEY)
    except UnicodeDecodeError:
        pass
