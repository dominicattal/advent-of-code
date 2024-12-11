A = []
B = []
C = []

with open("input.txt", "r") as txt:
    for line in txt:
        p = line.strip()
        if len(p) == 0: 
            continue
        if p[2] == ',':
            nums = map(int, p.split(','))
            C.append(tuple(nums))
        if p[2] == '|':
            a,b = p.split('|')
            A.append(int(a))
            B.append(int(b))

res = 0
for c in C:
    seen = set()
    valid = True
    for n in c:
        for i, a in enumerate(A):
            if a == n and B[i] in seen:
                valid = False
                break
        if not valid:
            break
        seen.add(n)
    print(c, valid)
    if valid:
        res += c[len(c)//2]
print(res)