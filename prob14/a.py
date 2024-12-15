import re

def prob1():
    w, h = 101, 103
    A = [[0] * w for _ in range(h)]
    R = []
    with open("in2.txt", "r") as txt:
        for line in txt:
            x, y, dx, dy = map(int, re.findall("-?[0-9]+", line))
            A[y][x] += 1
            R.append([x, y, dx, dy])
    for _ in range(1000):
        for i, r in enumerate(R):
            x, y, dx, dy = r
            A[y][x] -= 1
            x, y = (x+dx)%w, (y+dy)%h
            A[y][x] += 1
            R[i] = [x, y, dx, dy]
    Q = [0, 0, 0, 0]
    for r in R:
        x, y = r[0], r[1]
        dx, dy = (x - w // 2), (y - h // 2)
        if dx > 0 and dy > 0:
            Q[0] += 1
        elif dx < 0 and dy > 0:
            Q[1] += 1
        elif dx > 0 and dy < 0:
            Q[2] += 1
        elif dx < 0 and dy < 0:
            Q[3] += 1
    print(Q[0] * Q[1] * Q[2] * Q[3])

from PIL import Image
import numpy as np

def prob2():
    w, h = 101, 103
    A = [[0] * w for _ in range(h)]
    R = []
    with open("in2.txt", "r") as txt:
        for line in txt:
            x, y, dx, dy = map(int, re.findall("-?[0-9]+", line))
            A[y][x] += 1
            R.append([x, y, dx, dy])
    images = []
    for k in range(w * h):
        for i, r in enumerate(R):
            x, y, dx, dy = r
            A[y][x] -= 1
            x, y = (x+dx)%w, (y+dy)%h
            A[y][x] += 1
            R[i] = [x, y, dx, dy]
        a = np.zeros((h, w)).astype(np.ubyte)
        for i in range(h):
            for j in range(w):
                if A[i][j] == 0:
                    a[i][j] = 255
        im = Image.fromarray(a, mode="L")
        im.save(f"images/{k+1}.png")
        images.append(im)

    images[0].save("out.gif", save_all=True, append_images=images[1:], duration=100, loop=0)

#prob1
prob2()