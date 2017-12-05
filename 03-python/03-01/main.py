#!/usr/bin/env python

moves = {"right": {"x": "+", "y": None},  "up": {"x": None, "y": "+"}, "left": {"x": "-", "y": None}, "down": {"x": None, "y": "-"}}
order = ("right", "up", "left", "down")

def move(action, pos):
    m = moves[order[action]]
    #print(m, order[action])
    if m["x"] == "+":
        pos["x"] = pos["x"] + 1
    if m["x"] == "-":
        pos["x"] = pos["x"] - 1
    if m["y"] == "+":
        pos["y"] = pos["y"] + 1
    if m["y"] == "-":
        pos["y"] = pos["y"] - 1
    
    return pos

def main():
    pos = {"x": 0, "y": 0}
    num = 1
    index = 0
    factor = 1
    tick = 1
    while num <= 289326:
        for _ in range(factor):
            pos = move(index, pos)
            num = num + 1
            if num == 289326:
                print(pos, num)
                print(abs(pos['x']) + abs(pos['y']))

        if index == 3:
            index = 0
        else:
            index = index + 1
        
        if tick % 2 == 0:
            factor = factor + 1

        tick = tick + 1

main()