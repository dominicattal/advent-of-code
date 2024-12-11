A = []
with open("in2.txt", "r") as txt:
    for line in txt:
        A.append(list(line.strip()))

def prob1():

    D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def bfs(ii, jj):
        queue = [(ii, jj)]
        seen = set()
        while queue:
            i, j = queue.pop(0)
            if A[i][j] == '9':
                seen.add((i, j))
                continue
            for d in D:
                if 0 <= i + d[0] < len(A) and 0 <= j + d[1] < len(A[0]) and int(A[i+d[0]][j+d[1]]) == (int(A[i][j])+1):
                    queue.append((i+d[0], j+d[1]))
        return len(seen)

        
    res = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == '0':
                res += bfs(i, j)
    
    print(res)

def prob2():
    
    D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def bfs(ii, jj):
        queue = [(ii, jj)]
        res = 0
        while queue:
            i, j = queue.pop(0)
            if A[i][j] == '9':
                res += 1
                continue
            for d in D:
                if 0 <= i + d[0] < len(A) and 0 <= j + d[1] < len(A[0]) and int(A[i+d[0]][j+d[1]]) == (int(A[i][j])+1):
                    queue.append((i+d[0], j+d[1]))
        return res

        
    res = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == '0':
                res += bfs(i, j)
    
    print(res)

prob1()
prob2()