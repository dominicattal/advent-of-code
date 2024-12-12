A = []

with open("in1.txt", "r") as txt:
    for line in txt:
        A.append(list(line.strip()))

def prob1():
    seen = [[False] * len(A[0]) for _ in range(len(A))]

    D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def dfs(ii, jj):
        area = peri = 0
        q = [(ii, jj)]
        c = A[ii][jj]
        while q:
            i, j = q.pop(0)
            if not seen[i][j]:
                seen[i][j] = True
                area += 1
                for d in D:
                    if 0 <= i + d[0] < len(A) and 0 <= j + d[1] < len(A[0]):
                        if A[i+d[0]][j+d[1]] == c:
                            q.append((i+d[0], j+d[1]))
                        else:
                            peri += 1
                    else:
                        peri += 1
        return area * peri


    res = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if not seen[i][j]:
                res += dfs(i, j)
    print(res)

def prob2():
    seen = [[False] * len(A[0]) for _ in range(len(A))]

    def getArea(ii, jj, I):
        area = peri = 0
        q = [(ii, jj)]
        c = A[ii][jj]
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            i, j = q.pop(0)
            if not seen[i][j]:
                seen[i][j] = True
                A[i][j] = I
                area += 1
                for d in D:
                    if 0 <= i + d[0] < len(A) and 0 <= j + d[1] < len(A[0]):
                        if A[i+d[0]][j+d[1]] == c:
                            q.append((i+d[0], j+d[1]))
        return area

    def getPerimeter(c):
        peri = 0
        # west edge
        on_edge = False
        for i in range(len(A)):
            if A[i][0] == c and not on_edge:
                peri += 1
                on_edge = True
            elif A[i][0] != c:
                on_edge = False
        on_edge = False
        # east edge
        for i in range(len(A)):
            if A[i][-1] == c and not on_edge:
                peri += 1
                on_edge = True
            elif A[i][-1] != c:
                on_edge = False
        # north edge
        on_edge = False
        for j in range(len(A[0])):
            if A[0][j] == c and not on_edge:
                peri += 1
                on_edge = True
            elif A[0][j] != c:
                on_edge = False
        # south edge
        on_edge = False
        for j in range(len(A[0])):
            if A[-1][j] == c and not on_edge:
                peri += 1
                on_edge = True
            elif A[-1][j] != c:
                on_edge = False

        m, n = len(A), len(A[0])
        for i in range(m-1):
            on_edge = False
            for j in range(n):
                if A[i][j] == c and A[i+1][j] != c and not on_edge:
                    peri += 1
                    on_edge = True
                elif A[i][j] != c or A[i+1][j] == c:
                    on_edge = False
        for i in range(m-1,0,-1):
            on_edge = False
            for j in range(n):
                if A[i][j] == c and A[i-1][j] != c and not on_edge:
                    peri += 1
                    on_edge = True
                elif A[i][j] != c or A[i-1][j] == c:
                    on_edge = False
        for j in range(n-1):
            on_edge = False
            for i in range(m):
                if A[i][j] == c and A[i][j+1] != c and not on_edge:
                    peri += 1
                    on_edge = True
                elif A[i][j] != c or A[i][j+1] == c:
                    on_edge = False
        for j in range(n-1,0,-1):
            on_edge = False
            for i in range(m):
                if A[i][j] == c and A[i][j-1] != c and not on_edge:
                    peri += 1
                    on_edge = True
                elif A[i][j] != c or A[i][j-1] == c:
                    on_edge = False
        return peri
    
    res = 0
    I = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if not seen[i][j]:
                area = getArea(i, j, I)
                peri = getPerimeter(I)
                res += area * peri
                I += 1
    print(res)

prob1()
prob2()