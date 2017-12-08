#!/usr/bin/env python
import sys

programs = []
children = []
with open("main.txt") as f:
    for line in f.readlines():
        parse = line.strip().split("->")
        if len(parse) == 2:
            programs.append(dict([(parse[0].split()[0], [x.strip(',') for x in parse[1].split()])]))

for i in programs:
    for k,v in i.items():
        print(v)
        for x in v:
            if x not in children:
                children.append(x)

for i in programs:
    for k,v in i.items():
        if k not in children:
            print(k)


