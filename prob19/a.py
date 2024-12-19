def prob1():
    txt = open("in1.txt", "r")
    pats = txt.readline().strip().split(", ")
    def dfs(P):
        if P == "":
            return True
        valid = False
        for pat in pats:
            n = len(pat)
            if n <= len(P) and P[:n] == pat:
                valid = valid or dfs(P[n:])
        return valid
    res = 0
    line = txt.readline()
    for line in txt:
        if dfs(line.strip()):
            res += 1
    print(res)

def prob2():
    txt = open("in2.txt", "r")
    pats = txt.readline().strip().split(", ")
    def dfs(P):
        dp = [0] * (len(P) + 1)
        dp[0] = 1
        for i in range(1, len(P)+1):
            for j, pat in enumerate(pats):
                k = len(pat)
                if i - k >= 0 and P[i-k:i] == pat:
                    dp[i] += dp[i-k]
        return dp[len(P)]
    res = 0
    line = txt.readline()
    for line in txt:
        k = dfs(line.strip())
        res += k
    print(res)

def prob22():
    txt = open("in2.txt", "r")
    pats = txt.readline().strip().split(", ")
    def dfs(P):
        if P == "":
            return 1
        res = 0
        for pat in pats:
            n = len(pat)
            if n <= len(P) and P[:n] == pat:
                res += dfs(P[n:])
        return res
    res = 0
    line = txt.readline()
    for line in txt:
        print(line)
        res += dfs(line.strip())
    print(res)

prob2()