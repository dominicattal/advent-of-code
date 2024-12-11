from collections import defaultdict
from itertools import combinations

def prob1():
    d = defaultdict(list)
    w = h = 0
    with open("in1.txt", "r") as txt:
        for i, line in enumerate(txt):
            w += 1
            line = line.strip()
            h = 0
            for j, c in enumerate(line):
                h += 1
                if c != '.':
                    d[c].append((i, j))
    L = set()
    for a, b in d.items():
        C = combinations(b, 2)
        for c in C:
            p1, p2 = c
            x1 = y1 = x2 = y2 = 0
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            x1, y1 = p1[0] - dx, p1[1] - dy
            x2, y2 = p2[0] + dx, p2[1] + dy
            if 0 <= x1 < w and 0 <= y1 < h:
                L.add((x1, y1))
            if 0 <= x2 < w and 0 <= y2 < h:
                L.add((x2, y2))
    print(len(L))

def prob2():
    d = defaultdict(list)
    w = h = 0
    with open("in2.txt", "r") as txt:
        for i, line in enumerate(txt):
            w += 1
            line = line.strip()
            h = 0
            for j, c in enumerate(line):
                h += 1
                if c != '.':
                    d[c].append((i, j))
    L = set()
    for a, b in d.items():
        C = combinations(b, 2)
        for c in C:
            p1, p2 = c
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            i = 1
            while 0 <= p1[0] - i * dx < w and 0 <= p1[1] - i * dy < h:
                L.add((p1[0] - i * dx, p1[1] - i * dy))
                i += 1
            i = 1
            while 0 <= p2[0] + i * dx < w and 0 <= p2[1] + i * dy < h:
                L.add((p2[0] + i * dx, p2[1] + i * dy))
                i += 1
    print(len(L))

prob1()
prob2()