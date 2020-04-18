#!/usr/bin/python3

from string import ascii_lowercase
from subprocess import Popen, PIPE, STDOUT

counts = list()
digits = 0
for c in ascii_lowercase:
    p = Popen(
	"grep -ci "+c+" chiffrat.txt",
	shell=True,
	stdin=PIPE,
	stdout=PIPE,
	stderr=STDOUT,
	close_fds=True
    )
    count = p.stdout.read().decode('utf-8')
    # get number of digits for leading zeros at later print
    if len(count) > digits:
        digits = len(count)

    # add as tuple to list
    counts.append((c, int(count)))

allsum = sum(i for _, i in counts)
one_percent = allsum / 100

print("all:", allsum)
for count in counts:
    relative = round(count[1] / one_percent, 2)
    print(
	"character:", count[0],
	"absolute:", str(count[1]).zfill(digits),
	"relative:", relative
    )
