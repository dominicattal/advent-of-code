from collections import Counter

l1, l2 = [], []
for i in range(1000):
    n1, n2 = map(int, input().split())
    l1.append(n1)
    l2.append(n2)
l1.sort()
l2.sort()
res = 0
for i in range(1000):
    res += abs(l2[i]-l1[i])
print(res)

C = Counter(l2)

res = 0
for n in l1:
    res += C[n] * n
print(res)