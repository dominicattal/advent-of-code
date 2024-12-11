res = 0
with open("nums.txt", "r") as txtfile:
    for line in txtfile:
        a, b = map(int, line.split())
        res += a * b
print(res)