nums = []

def solve(A):
    s = A.split(" ")
    t = int(s[0][:-1])
    B = list(map(int, s[1:]))
    for m in range(1<<(len(B)-1)):
        q = B[0]
        for i in range(len(B)-1):
            if m & (1<<i):
                q += B[i+1]
            else:
                q *= B[i+1]
        if q == t:
            return t
    return 0

res = 0
with open("input.txt") as txt:
    for line in txt:
        res += solve(line.strip())
print(res)