#!/usr/bin/python3

from string import ascii_lowercase
from collections import OrderedDict

filename = "chiffrat.txt"
all_characters = ascii_lowercase + 'äöüß'
char_count = dict()
allsum = 0

with open(filename, 'r') as infile:
    for line in infile:
        for char in line:
            for achar in all_characters:
                if achar == char.lower():
                    allsum += 1
                    if not achar in char_count:
                        char_count[achar] = 1
                    else:
                        char_count[achar] += 1


one_percent = allsum / 100

print("all:", allsum)

schar_count = OrderedDict(sorted(char_count.items(), key=lambda x:x[1], reverse=True))

for curchar in schar_count:
    relative = round(char_count[curchar] / one_percent, 2)
    print(
	"character:", curchar,
	"absolute:", (str(char_count[curchar])).rjust(2),
	"relative:", relative
    )
