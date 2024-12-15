def prob1():
    A = []
    B = ""
    x, y = 0, 0
    with open("in3.txt", "r") as txt:
        read_map = True
        for i, line in enumerate(txt):
            if len(line) == 1:
                read_map = False
            elif read_map:
                for j in range(len(line)):
                    if line[j] == '@':
                        x, y = i, j
                A.append(list(line.strip()))
            else:
                B += line.strip()
    
    D = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
    def check(x, y, dx, dy):
        while 0 <= x < len(A) and 0 <= y < len(A[0]):
            if A[y][x] == '.':
                return True
            elif A[y][x] == '#':
                return False
            x += dx
            y += dy
        return False
            
    def move(x, y, dx, dy):
        c1, c2 = A[y][x], '.'
        while c1 != '.':
            A[y][x] = c2
            x, y = x+dx, y+dy
            c1, c2, A[y][x] = A[y][x], c1, c1

    for c in B:
        dx, dy = D[c]
        if check(x, y, dx, dy):
            move(x, y, dx, dy)
            x += dx
            y += dy

    res = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == "O":
                res += 100 * i + j
    print(res)

def prob2():
    A = []
    B = ""
    x, y = 0, 0
    M = {"#": "##", "O": "[]", ".":"..", "@": "@."}
    with open("in3.txt", "r") as txt:
        read_map = True
        for i, line in enumerate(txt):
            if len(line) == 1:
                read_map = False
            elif read_map:
                for j in range(len(line)):
                    if line[j] == '@':
                        x, y = 2 * j, i
                s = ""
                for c in line.strip():
                    s += M[c]
                A.append(list(s))
            else:
                B += line.strip()
    
    print(x, y)
    for a in A:
        print("".join(a))
    print()

    D = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}

    def blocked(x, y, dy):
        if not 0 <= x < len(A[0]) or not 0 <= y < len(A):
            return True
        elif A[y][x] == '@':
            return blocked(x, y+dy, dy)
        elif A[y][x] == '.':
            return False
        elif A[y][x] == '#':
            return True
        elif A[y][x] == '[':
            return blocked(x, y+dy, dy) or blocked(x+1, y+dy, dy)
        elif A[y][x] == ']':
            return blocked(x, y+dy, dy) or blocked(x-1, y+dy, dy)
        return True

    def check(x, y, dx, dy):
        if dy == 0:
            while 0 <= y < len(A) and 0 <= x < len(A[0]):
                if A[y][x] == '.':
                    return True
                elif A[y][x] == '#':
                    return False
                x += dx
                y += dy
            return False
        return not blocked(x, y, dy)

    def move_other(x, y, dy, c1, c2):
        if A[y][x] == '@':
            c1, A[y][x] = A[y][x], c2
            move_other(x, y+dy, dy, A[y][x], '@')
        elif A[y][x] == '.':
            A[y][x] = c2
        elif A[y][x] == '#':
            return
        elif A[y][x] == '[':
            c1, A[y][x] = A[y][x], c2
            move_other(x, y+dy, dy, A[y][x], '[')
            c1, A[y][x+1] = A[y][x+1], '.'
            move_other(x+1, y+dy, dy, A[y][x+1], ']')
        elif A[y][x] == ']':
            c1, A[y][x] = A[y][x], c2
            move_other(x, y+dy, dy, A[y][x], ']')
            c1, A[y][x-1] = A[y][x-1], '.'
            move_other(x-1, y+dy, dy, A[y][x-1], '[')

    def move(x, y, dx, dy):
        if dy == 0:
            c1, c2 = A[y][x], '.'
            while c1 != '.':
                A[y][x] = c2
                x, y = x+dx, y+dy
                c1, c2, A[y][x] = A[y][x], c1, c1
            return
        move_other(x, y, dy, A[y][x], '.')

    for c in B:
        dx, dy = D[c]
        if check(x, y, dx, dy):
            move(x, y, dx, dy)
            x += dx
            y += dy
        """ print(c, x, y, dx, dy)
        for a in A:
            print("".join(a))
        print() """

    res = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == "[":
                res += 100 * i + j
    print(res)

prob2()