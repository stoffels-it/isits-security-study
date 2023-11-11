#!/usr/bin/python3
import re
import sys


sbox = []
for line in sys.stdin:
    binary = re.split("\\s+|\\n+", line.strip())
    if len(binary[0]) == 2:
        # row index was found and has to be removed
        del(binary[0])
    decimal = []
    for b in binary:
        decimal.append(str("%02d" % (int(b,2))))
    sbox.append(decimal)

for s in sbox:
    print(" ".join(s))
