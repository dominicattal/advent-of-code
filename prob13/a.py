import re

def prob1():
    
    A = []
    with open("in2.txt", "r") as txt:
        B = txt.readlines()
        for i in range(0, len(B), 4):
            ax, ay = map(int, re.findall("[0-9]+", B[i]))
            bx, by = map(int, re.findall("[0-9]+", B[i+1]))
            tx, ty = map(int, re.findall("[0-9]+", B[i+2]))
            A.append((ax, ay, bx, by, tx, ty))

    res = 0
    while A:
        ax, ay, bx, by, tx, ty = A.pop()
        m = 1000000
        for m1 in range(101):
            for m2 in range(101):
                if (ax * m1 + bx * m2) == tx and (ay * m1 + by * m2) == ty:
                    m = min(m, m1*3+m2)
        if m != 1000000:
            res += m
    
    print(res)

def bezout(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t

def prob2():
    res = 0
    """
    x1 * ax + y1 * bx = tx
    x2 * ay + y2 * by = ty

    x - k * dx == 0
    k == x / dx
    """
    with open("in2.txt", "r") as txt:
        B = txt.readlines()
        for i in range(0, len(B), 4):
            ax, ay = map(int, re.findall("[0-9]+", B[i]))
            bx, by = map(int, re.findall("[0-9]+", B[i+1]))
            tx, ty = map(lambda x : int(x) + 10000000000000, re.findall("[0-9]+", B[i+2]))
            #print(ax, ay, bx, by, tx, ty)
            d1, x1, y1 = bezout(ax, bx)
            dx1, dy1 = bx // d1, ax // d1
            x1 *= tx // d1
            y1 *= tx // d1
            k1 = x1 // dx1
            #print(dx1, dy1, x1 - k1 * dx1, y1 + k1 * dy1)
            d2, x2, y2 = bezout(ay, by)
            dx2, dy2 = by // d2, ay // d2
            x2 *= ty // d2 
            y2 *= ty // d2
            k2 = x2 // dx2
            #print(dx2, dy2, x2 - k2 * dx2, y2 + k2 * dy2)

            #cramers rule
            a1 = dx1
            b1 = -dx2
            c1 = (x2 - k2 * dx2) - (x1 - k1 * dx1)
            a2 = dy1
            b2 = -dy2
            c2 = (y1 + k1 * dy1) - (y2 + k2 * dy2)
            num_x = (c1*b2 - b1*c2)
            den_x = (a1*b2 - b1*a2)
            num_y = (a1*c2 - c1*a2)
            den_y = (a1*b2 - b1*a2)
            if num_x % den_x == 0 and num_y % den_y == 0:
                x = num_x // den_x
                y = num_y // den_y
                #print(x, y)
                m1 = dx1 * x + (x1 - k1 * dx1)
                m2 = (y1 + k1 * dy1) - dy1 * x
                res += 3 * m1 + m2

    print(res)

def prob22():
    with open("in1.txt", "r") as txt:
        B = txt.readlines()
        for i in range(0, len(B), 4):
            ax, ay = map(int, re.findall("[0-9]+", B[i]))
            bx, by = map(int, re.findall("[0-9]+", B[i+1]))
            tx, ty = map(lambda x : int(x) + 10000000000000, re.findall("[0-9]+", B[i+2]))
            l, r = 0, 10000000000000
            min_m = None
            while l < r:
                m1 = (l + r) // 2
                m2 = (tx - bx * m1) // ax
                print(m1, m2, ax * m1 + bx * m2, tx, ax * m1 + bx * m2 - tx)
                if m2 < 0 or ax * m1 + bx * m2 < tx:
                    r = m1 - 1
                elif ax * m1 + bx * m2 > tx:
                    l = m1 + 1
                else:
                    r = m1 - 1
                    min_m = m1
            print(min_m)
            m1 = (l + r) // 2
            m2 = (tx - bx * m1) // ax
            print(ax * m1 + bx * m2, tx)

#prob1()
prob2()
#prob22()