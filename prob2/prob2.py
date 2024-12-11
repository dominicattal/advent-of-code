n = 1000
res = 0

def S(arr):
    print(arr)
    inc = arr[1] > arr[0]
    for j in range(1, len(arr)):
        if inc and not 1 <= arr[j] - arr[j-1] <= 3:
            return False
        elif not inc and not 1 <= arr[j-1] - arr[j] <= 3:
            return False
    return True

def T(arr):
    if S(arr): return True
    for j in range(len(arr)):
        if S(arr[:j]+arr[j+1:]):
            return True
    return False

for _ in range(n):
    L = list(map(int, input().split()))
    print("!!!!")
    print(L)
    if T(L):
        res += 1
    
print(res)