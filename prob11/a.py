from functools import cache

def prob1():
    S = [9759, 0, 256219, 60, 1175776, 113, 6, 92833]
    for _ in range(25):
        T = []
        for s in S:
            if s == 0:
                T.append(1)
            elif len(str(s)) % 2 == 0:
                T.append(int(str(s)[:len(str(s))//2]))
                T.append(int(str(s)[len(str(s))//2:]))
            else:
                T.append(s*2024)
        S = T

    print(len(S))

def prob2():
    S = [0]

    @cache
    def dp(n, d=0):
        if d == 75:
            return 1
        if n == 0:
            return dp(1, d+1)
        elif len(str(n)) % 2 == 0:
            n1 = int(str(n)[:len(str(n))//2])
            n2 = int(str(n)[len(str(n))//2:])
            return dp(n1, d+1) + dp(n2, d+1)
        return dp(n*2024, d+1)
    
    print(sum(map(dp, S)))

import numpy as np

def prob3():
    N = 25
    S = [9759, 0, 256219, 60, 1175776, 113, 6, 92833]
    U = {}
    q = [s for s in S]
    idx = 0
    while q:
        m = q.pop(0)
        if m not in U:
            if m == 0:
                U[m] = (idx, [1])
                q.append(1)
            elif len(str(m)) % 2 == 0:
                m1 = int(str(m)[:len(str(m))//2])
                m2 = int(str(m)[len(str(m))//2:])
                U[m] = (idx, [m1, m2])
                q.extend([m1, m2])
            else:
                U[m] = (idx, [m * 2024])
                q.append(m * 2024)
            idx += 1
    
    m = len(U)
    mat = np.zeros((m, m)).astype(int)
    for k1, v in U.items():
        idx1 = v[0]
        for k2 in v[1]:
            idx2 = U[k2][0]
            mat[idx1, idx2] += 1

    v = np.zeros(m).astype(int)
    for s in S:
        v[U[s][0]] += 1
    for _ in range(N):
        v = np.dot(v, mat)
    print(v.sum())

#prob1()
#prob2()
prob3()