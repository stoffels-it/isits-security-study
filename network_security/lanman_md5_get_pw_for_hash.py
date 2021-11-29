#!/usr/bin/python3

import hashlib


check_pw = 22334455
constant = "NetSec1"

check_hash = "c98484bc0ee0509fda498b1fe098c2c3"
find_hash = "6397eee0332708a6edf44e10a559586b"


def md5(password, constant):
    m = hashlib.md5()
    m.update(str.encode(password + constant))
    return m.hexdigest()


def get_lanman_hash(pw, constant):
   # pad with 0 to create 14 Byte string
   # usually, in lanman, the nullbyte would be used:
   ### padded = str(pw).ljust(14, '\0').upper()
   # but in this exercise, the 0 char is used
   padded = str(pw).ljust(14, '0').upper()
   leftpw = padded[0:7]
   lefthash = md5(leftpw, constant)[0:16]

   rightpw = padded[7:14]
   righthash = md5(rightpw, constant)[0:16]
   return lefthash + righthash


check = (get_lanman_hash(check_pw, constant) == check_hash)
print("implementation check result is:", check)

for pw in range(000000000, 999999999):
    result = get_lanman_hash(pw, constant)
    if result == find_hash:
        print("requested pw is:", pw)
