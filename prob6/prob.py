si, sj = 0, 0
M = []
with open("input.txt", "r") as txt:
    for i, line in enumerate(txt):
        line = line[:-1]
        M.append(list(line))
        for j in range(len(line)):
            if line[j] == '^':
                si, sj = i, j

D = [(1, 0), (0, -1), (-1, 0), (0, 1)]
d = 2
while True:
    while 0 <= si + D[d][0] < len(M) and 0 <= sj + D[d][1] < len(M[0]) and M[si+D[d][0]][sj+D[d][1]] != '#':
        M[si][sj] = 'X'
        si += D[d][0]
        sj += D[d][1]
    if not 0 <= si + D[d][0] < len(M) or not 0 <= sj + D[d][1] < len(M[0]):
        break
    d = (d + 1) % 4

res = 1
for m in M:
    for n in m:
        if n == 'X':
            res += 1

print(res)