import sys

input = sys.argv[1]
l = [int(i) for i in str(input)]
c, s = 0, 0
for i in l:
    if c == len(l) - 1 and i == l[0]:
        s += i
    elif i == l[c + 1]:
        s += i
    c += 1
print(s)

