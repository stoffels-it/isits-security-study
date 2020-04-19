#!/usr/bin/python3
# capture_output for subprocess.run requires at least python3.7

from string import ascii_lowercase
from subprocess import run

counts = list()
digits = 0
all_characters = ascii_lowercase + 'äöüß'
for char in all_characters:
    p = run(
	["grep", "-ci", char, "chiffrat.txt"],
	capture_output=True,
    )
    count = p.stdout
    # get number of digits for leading whitespaces at later print
    if len(count) > digits:
        digits = len(count)

    # add as tuple to list
    counts.append((char, int(count)))

allsum = sum(count for _, count in counts)
one_percent = allsum / 100

print("all:", allsum)
for char,count in counts:
    relative = round(count / one_percent, 2)
    print(
	"character:", char,
	"absolute:", (str(count)).rjust(digits),
	"relative:", relative
    )
