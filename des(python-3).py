from pyDes import *
import binascii

print("Jay's DES & 3DES Calculator")
data = input("Input Data: ")
k1 = input("Input Key : ")

data = str(data)


#k1 = k1.decode("hex")
k1 = bytes.fromhex(k1).decode('utf-8')

print("Key Length is : " + str(len(k1)))

if len(k1) > 8:
	print("########## Performing 3DES ##########")
	k = triple_des( k1, ECB, "\0\0\0\0\0\0\0\0")
	d = k.encrypt(data)
	hex = str(binascii.hexlify(d))
	#print "Encrypted: %r" % d
	formatted_hex = ' : '.join(hex[i:i+2] for i in range(0, len(hex), 2))
	print(formatted_hex)
	print("Decrypted ACII Value : %r" % k.decrypt(d))
	#assert k.decrypt(d) == data
else :
	print("########## Performing DES ##########")
	k = des( k1, ECB, "\0\0\0\0\0\0\0\0")
	d = k.encrypt(data)
	hex = str(binascii.hexlify(d))
	#print "Encrypted: %r" % d
	formatted_hex = ' : '.join(hex[i:i+2] for i in range(0, len(hex), 2))
	print(formatted_hex)
	#print(binascii.b2a_hex(d))
	#print(bytes.fromhex(str(d)))
	#print("Encrypted Hex Value:" + str(" ".join(hex(ord(n)) for n in d)))
	#print("Encrypted Hex Value:" + str(" ".join(hex(ord(n)) for n in d)))
	print("Decrypted ACII Value : %r" % k.decrypt(d))
	#assert k.decrypt(d) == data
