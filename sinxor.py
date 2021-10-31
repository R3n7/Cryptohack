from binascii import unhexlify 
def byte_xor(ba1):
	for i in range(256):
    		print(bytes([_a ^ i for _a in ba1]))
#en = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

end = '1314190e1c1001024a0825194e145d0e251849251f4e091316032518084a11491407'
encoded = unhexlify(end)
byte_xor(encoded)