A = [set() for _ in range(100)]
B = []

with open("input.txt", "r") as txt:
    for line in txt:
        p = line.strip()
        if len(p) == 0: 
            continue
        if p[2] == ',':
            nums = list(map(int, p.split(',')))
            B.append(nums)
        if p[2] == '|':
            a,b = map(int, p.split('|'))
            A[b].add(a)

res = 0
for b in B:
    valid = True
    for i in range(len(b)):
        # find first instance
        j = 0
        while j < i and b[i] not in A[b[j]]:
            j += 1
        if j < i:
            valid = False
        # shift
        tmp = b[j]
        b[j] = b[i]
        j += 1
        while j <= i:
            tmp1 = b[j]
            b[j] = tmp
            tmp = tmp1
            j += 1
    if not valid:
        res += b[len(b)//2]

print(res)