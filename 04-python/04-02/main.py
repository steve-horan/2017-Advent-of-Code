#!/usr/bin/env python

c = 0
with open("main.txt") as f:
    for x in f.readlines():
        l = [''.join(sorted(i)) for i in x.strip().split()]
        print(l)
        b = len(l)
        a = len(set(l))

        if b == a:
           c = c + 1         

print(c)
