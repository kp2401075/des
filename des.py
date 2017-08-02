from pyDes import *

print "Jay's DES & 3DES Calculator"
data = raw_input("Input Data: ")
k1 = raw_input("Input Key : ")

data = str(data)


k1 = k1.decode("hex")
print "Key Length is : " + str(len(k1))
if len(k1) > 8:
	print "########## Performing 3DES ##########"
	k = triple_des( k1, ECB, "\0\0\0\0\0\0\0\0")
	d = k.encrypt(data)
	#print "Encrypted: %r" % d
	print "Encrypted Hex Value:" + str(" ".join(hex(ord(n)) for n in d))
	print "Decrypted ACII Value : %r" % k.decrypt(d)
	assert k.decrypt(d) == data
else :
	print "########## Performing DES ##########"
	k = des( k1, ECB, "\0\0\0\0\0\0\0\0")
	d = k.encrypt(data)
	#print "Encrypted: %r" % d
	print "Encrypted Hex Value:" + str(" ".join(hex(ord(n)) for n in d))
	#print "Encrypted Hex Value: ".join(hex(ord(n)) for n in d)
	print "Decrypted ACII Value : %r" % k.decrypt(d)
	assert k.decrypt(d) == data
