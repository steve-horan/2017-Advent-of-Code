import sys

input = sys.argv[1]
l = [int(i) for i in str(input)]
c, s = 0, 0
for i in l:
    h = (len(l) / 2) + c
    if c >= (len(l) / 2):
        break
    elif i == l[h]:
        s += i * 2
    c += 1
print(s)

