#!/usr/bin/python3
# A hash is given and compared with hashes generated from a password
# dictionary to determine the password. The hashes are without salt.

import hashlib

searchpw = '46256e1e9f868bce7e89cef99004c1600e17da2e'

with open('common_passwords.txt') as file:
    lines = file.read().splitlines()

for line in lines:
    h = hashlib.sha1(line.encode('utf-8')).hexdigest()
    if h == searchpw:
        print("password found: %s" % line)
