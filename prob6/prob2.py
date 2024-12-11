ssi, ssj = 0, 0
M = []
with open("input.txt", "r") as txt:
    for i, line in enumerate(txt):
        line = line[:-1]
        M.append(list(line))
        for j in range(len(line)):
            if line[j] == '^':
                ssi, ssj = i, j

D = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def tryt(si, sj):
    seen = set()
    d = 2
    while True:
        if (si, sj, d) in seen:
            return 1
        seen.add((si, sj, d))
        while 0 <= si + D[d][0] < len(M) and 0 <= sj + D[d][1] < len(M[0]) and M[si+D[d][0]][sj+D[d][1]] != '#':
            M[si][sj] = 'X'
            si += D[d][0]
            sj += D[d][1]
        if not 0 <= si + D[d][0] < len(M) or not 0 <= sj + D[d][1] < len(M[0]):
            break
        d = (d + 1) % 4
    return 0

def reset():
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 'X':
                M[i][j] = '.'

def main():
    res = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == '.':
                M[i][j] = '#'
                res += tryt(ssi, ssj)
                M[i][j] = '.'
                reset()

    print(res)

main()