A = []
with open("input.txt", "r") as txtfile:
    for line in txtfile:
        A.append(list(line.strip()))

m, n = len(A), len(A[0])
print(m, n)

res = 0
def cond1(i, j):
    return (A[i-1][j-1] == 'M' and A[i+1][j+1] == 'S') or (A[i-1][j-1] == 'S' and A[i+1][j+1] == 'M')
def cond2(i, j):
    return (A[i+1][j-1] == 'M' and A[i-1][j+1] == 'S') or (A[i+1][j-1] == 'S' and A[i-1][j+1] == 'M')
for i in range(1,m-1):
    for j in range(1,n-1):
        if A[i][j] == 'A' and cond1(i, j) and cond2(i, j):
            res += 1
print(res)