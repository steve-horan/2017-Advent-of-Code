#!/usr/bin/env python
import sys

with open("main.txt") as f:
   banks = [int(x) for x in f.readline().split("\t")]

def high_bank():
    return banks.index(max(banks))

configs_len = len(banks) - 1
configs = []
num = 0
found = False
dup = ""
found_num = 0
while True:
    bank_val = banks[high_bank()]
    start = high_bank()
    banks[high_bank()] = 0
    while bank_val != 0:
        if start >= configs_len:
            start = -1
        start = start + 1
        banks[start] = banks[start] + 1
        bank_val = bank_val - 1
    configs.append(''.join(str(x) for x in banks))
    num = num + 1
    if found:
        if configs[-1:] == dup:
            print(num - found_num)
            sys.exit(0)
    elif len(configs) != len(set(configs)):
            found = True
            dup = configs[-1:]
            found_num = num



        




