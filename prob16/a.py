from heapq import heappush, heappop
def prob1():
    A = []
    s = (0,0)
    with open("in1.txt", "r") as txt:
        for i, line in enumerate(txt):
            for j in range(len(line)):
                if line[j] == 'S':
                    s = (i, j)
            A.append(list(line.strip()))
    pq = []
    D = [(1,0),(0,1),(-1,0),(0,-1)]
    heappush(pq, (0, 1, s[0], s[1]))
    seen = set()
    while pq:
        score, d, x, y = heappop(pq)
        if A[x][y] == 'E':
            print(score, d, x, y)
            return score
        if (d,x, y) not in seen:
            seen.add((d,x,y))
            nx, ny = x+D[d][0], y+D[d][1]
            if 0 <= nx < len(A[0]) and 0 <= ny < len(A) and A[nx][ny] != '#':
                heappush(pq, (score+1,d,nx,ny))
            heappush(pq, (score+1000,(d+1)%4,x,y))
            heappush(pq, (score+1000,(d-1)%4,x,y))

def prob2():
    A = []
    s = (0,0)
    with open("in3.txt", "r") as txt:
        for i, line in enumerate(txt):
            for j in range(len(line)):
                if line[j] == 'S':
                    s = (j,i)
            A.append(list(line.strip()))
    for a in A:
        print("".join(a))
    pq = []
    V = [[[False] * 4 for i in range(len(A[0]))] for j in range(len(A))]
    D = [(1,0),(0,1),(-1,0),(0,-1)]
    heappush(pq, (0, 0, s[0], s[1], (1, s[0], s[1], 0)))
    while pq:
        score, d, x, y, path = heappop(pq)
        if not 0 <= x < len(A[0]) or not 0 <= y < len(A) or not A[y][x] != '#':
            continue
        if A[y][x] == 'E':
            break
        if not V[y][x][d]:
            V[y][x][d] = True
            heappush(pq, (score+1,d,x+D[d][0],y+D[d][1], path+(d,x+D[d][0],y+D[d][1],score+1)))
            heappush(pq, (score+1000,(d+1)%4,x,y,path+((d+1)%4,x,y,score+1000)))
            heappush(pq, (score+1000,(d-1)%4,x,y,path+((d-1)%4,x,y,score+1000)))
    INF = 10**9
    M = [[[INF] * 4 for i in range(len(A[0]))] for j in range(len(A))]
    N = [[[INF] * 4 for i in range(len(A[0]))] for j in range(len(A))]
    R = A.copy()
    res = set()
    for i in range(0, len(path), 4):
        d,x,y,score = path[i:i+4]
        M[y][x][d] = score
        R[y][x] = 'O'
        res.add((x,y))
    pq = []
    V = [[[False] * 4 for i in range(len(A[0]))] for j in range(len(A))]
    heappush(pq, (0, 0, s[0], s[1], (1, s[0], s[1], 0)))
    while pq:
        score, d, x, y, path = heappop(pq)
        if not 0 <= x < len(A[0]) or not 0 <= y < len(A) or not A[y][x] != '#':
            continue
        if score == M[y][x][d]:
            for i in range(0, len(path), 4):
                d2,x2,y2,score2 = path[i:i+4]
                M[y2][x2][d2] = score2
                R[y2][x2] = 'O'
                res.add((x2,y2))
        if A[y][x] == 'E':
            continue
        if score <= N[y][x][d]:
            N[y][x][d] = score
            heappush(pq, (score+1,d,x+D[d][0],y+D[d][1], path+(d,x+D[d][0],y+D[d][1],score+1)))
            heappush(pq, (score+1000,(d+1)%4,x,y,path+((d+1)%4,x,y,score+1000)))
            heappush(pq, (score+1000,(d-1)%4,x,y,path+((d-1)%4,x,y,score+1000)))
    for r in R:
        print("".join(r))
    print(len(res))

#prob1()
prob2()