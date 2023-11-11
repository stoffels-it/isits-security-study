#!/usr/bin/python3
from helpers import *


subf = "conv_tables/"
sbox_tables = []
for sbox_number in range(1, 9):
    filename = f"s{sbox_number}.txt"
    sbox_tables.append(read_table(subf+filename))


block = input("which bin value to convert?: ")
box_number = input("which s-box to use?: ")

col = int(block[1:5], 2)
row = int(block[0]+block[5], 2)
print("col:", col, "row", row)
entry = sbox_tables[int(box_number)-1][row][col]
print("sbox conversion to:", '{0:04b}'.format(entry))
