#!/usr/bin/env python

with open("work.txt") as f:
    s = 0
    for line in f:
        l = min([int(x) for x in line.split()])
        h = max([int(x) for x in line.split()])
        s += int(h) - int(l)
    print(s)


