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
    S = [9759, 0, 256219, 60, 1175776, 113, 6, 92833]

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
    

#prob1()
prob2()