import math
import re

def read_table(filepath: str, base: int = 10) -> list:
    with open(filepath, "r") as f:
        return [list(map(lambda y: int(y, base), re.split("\\s+", x.strip()))) for x in f.readlines()]


def generate_block(command: str, count: int = 64) -> str:
    out = 0
    if command.startswith("all"):
        digit = int(command[3])
        for i in range(0, count):
            out = out | (digit << i)
    elif command.startswith("generate"):
        digit = int(command[8])
        positions = command[10:].strip().split()
        if digit == 1:
            for pos in positions:
                out = out | (digit << (count - int(pos)))
    else:
        print("no command and no binary digit found!")
        exit(1)
    return format(out, f"0{count}b")


def as_blocks(mystr: str, width: int) -> str:
    i = 0
    j = width
    out = ""
    while j <= len(mystr):
        out += mystr[i:j] + " "
        i += width
        j += width
    return out

    
def scramble(inp: str, slist: list) -> str:
    # add trailing character for being able to use indexes
    # beginning with 1 according to the scramble table
    x = "#"+inp
    out = ""
    # do the scrambling according to DES' substitution table
    for row in slist:
        for entry in row:
            out += x[entry]
    return out

def permutation(inp: str, slist: list) -> str:
    # add trailing character for being able to use indexes
    # beginning with 1 according to the scramble table
    x = "#"+inp
    out = ""
    # do the scrambling according to DES' substitution table
    for row in slist:
        for entry in row:
            out += x[entry]
    return out
