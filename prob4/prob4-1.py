A = []
with open("input.txt", "r") as txtfile:
    for line in txtfile:
        A.append(list(line.strip()))

m, n = len(A), len(A[0])
T = "XMAS"
RT = T[::-1]
print(m, n)

res = 0
D = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
for i in range(m):
    for j in range(n):
        for d in D:
            if not 0 <= i + 3 * d[1] < m or not 0 <= j + 3* d[0] < n:
                continue
            s = A[i][j] + A[i+d[1]][j+d[0]] + A[i+2*d[1]][j+2*d[0]] + A[i+3*d[1]][j+3*d[0]]
            if s == T:
                res += 1
print(res)