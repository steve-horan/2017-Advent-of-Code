#!/usr/bin/env python


with open("main.txt") as f:
   register = [x.strip() for x in f.readlines()]

step = 0
index = 0
while index < len(register):
    currind = index
    curr = register[index]
    index = index + int(curr)
    if int(curr) >= 3:
        register[currind] = int(register[currind]) - 1
    else:
        register[currind] = int(register[currind]) + 1
    step = step + 1
    if index >= len(register):
        print(step)


