nums = []

def S(B, i, q, t):
    if i == len(B):
        if q == t:
            return t
        return 0
    add = S(B, i+1, q+B[i], t)
    mul = S(B, i+1, q*B[i], t)
    con = S(B, i+1, int(str(q)+str(B[i])), t)
    return max(add, mul, con)


def solve(A):
    s = A.split(" ")
    t = int(s[0][:-1])
    B = list(map(int, s[1:]))
    return S(B, 1, B[0], t)

res = 0
with open("input.txt") as txt:
    for line in txt:
        res += solve(line.strip())
print(res)