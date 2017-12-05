#!/usr/bin/env python
import sys
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

def calc_grid(pos, grid):
    loc = [
        {"north": {"x": 0, "y": 1}},
        {"northeast": {"x": 1, "y": 1}},
        {"east": {"x": 1, "y": 0}},
        {"southeast": {"x": 1, "y": -1}},
        {"south": {"x": 0, "y": -1}},
        {"southwest": {"x": -1, "y": -1}},
        {"west": {"x": -1, "y": 0}},
        {"northwest": {"x": -1, "y": 1}},
    ]

    summ = 0
    for d in loc:
        for k, v in d.items():
            newpos = {}
            newpos["x"] = v["x"] + pos["x"]
            newpos["y"] = v["y"] + pos["y"]
            
            for g in grid:
                if newpos["x"] == g["x"] and newpos["y"] == g["y"]:
                    summ = summ + g["n"]
    
    return summ


def main():
    pos = {"x": 0, "y": 0, "n": 1}
    index = 0
    factor = 1
    tick = 1
    grid = []
    grid.append(pos.copy())
    num = 1
    while True:
        for _ in range(factor):
            pos = move(index, pos)
            summ = calc_grid(pos, grid)
            pos["n"] = summ
            grid.append(pos.copy())
            num = num + 1
            if summ > 289326:
                print(summ)
                sys.exit(0)
                
        if index == 3:
            index = 0
        else:
            index = index + 1
        
        if tick % 2 == 0:
            factor = factor + 1

        tick = tick + 1

main()