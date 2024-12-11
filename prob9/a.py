A = ""
with open("in2.txt", "r") as txt:
    for line in txt:
        A = line.strip()
        

def prob1():
    S = []
    I = 0
    for i in range(0, len(A), 2):
        for j in range(int(A[i])):
            S.append(I)
        I += 1
    res = 0
    t = 0
    i = j = 0
    while S:
        k = int(A[i])
        for _ in range(k):
            if S:
                res += S.pop(0) * j if t == 0 else S.pop() * j
                j += 1
        t = 1 - t
        i += 1
    
    print(res)

def prob2():
    M = []
    I = 0
    for i in range(len(A)):
        if i % 2 == 0:
            M.extend([I] * int(A[i]))
            I += 1
        else:
            M.extend([-1] * int(A[i]))
    l = r = len(M) - 1
    while l > 0 and r > 0:
        while l > 0 and M[l-1] == M[r]:
            l -= 1
        k = r - l + 1
        for i in range(min(l, len(M)-k)):
            if all([M[i+j] == -1 for j in range(k)]):
                for j in range(k):
                    M[i+j], M[l+j] = M[l+j], -1
                break
        r = l = l - 1

    res = 0
    for i in range(len(M)):
        if M[i] != -1:
            res += M[i] * i
    print(res)

#prob1()
prob2()