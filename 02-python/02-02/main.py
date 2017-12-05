#!/usr/bin/env python

with open("work.txt") as f:
    s = 0
    for line in f:
        l = [int(x) for x in line.split()]
        for i in l:
            for x in l:
                if i % x == 0:
                    if i > x:
                        s += i / x
    print(s)


