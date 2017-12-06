#!/usr/bin/env python


with open("main.txt") as f:
   register = [x.strip() for x in f.readlines()]

step = 0
index = 0
while index < len(register):
    currind = index
    curr = register[index]
    index = index + int(curr)
    register[currind] = int(register[currind]) + 1
    step = step + 1
    print(step)


