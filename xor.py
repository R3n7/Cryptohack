from binascii import unhexlify 
def byte_xor(ba1,ba2):
    		return bytes([_a ^ _b for _a,_b in zip(ba1,ba2)])
en = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
encoded = unhexlify(en)
key = 'crypto{'.encode()
key1 = b'myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkey'
print(key)
print(key1)

print(byte_xor(encoded,key1))