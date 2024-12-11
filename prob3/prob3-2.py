enabled = True
res = 0
with open("nums2.txt", "r") as txtfile:
    for line in txtfile:
        line = line.strip()
        if line == "do":
            enabled = True
            continue
        if line == "don't":
            enabled = False
            continue
        if enabled:
            a, b = map(int, line.split())
            res += a * b
print(res)