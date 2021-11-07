#!/usr/bin/python3

cryptstring = input("Paste the crypted hex values here divided by whitespaces - e.g. '60 78 50...': ")
keystring = input("Paste the decryption key hex values here divided by whitespaces - e.g. '08 0C 24...': ")
cryptlist = cryptstring.split()
keylist = keystring.split()
decryptstring = ''

for i in range(0, len(cryptlist)):
    c = cryptlist[i]
    k = keylist[i]
    hex_c = int(c, 16)
    hex_k = int(k, 16)
    decryptstring = decryptstring + chr(hex_c ^ hex_k)

print("Decrypted ASCII:" decryptstring)
