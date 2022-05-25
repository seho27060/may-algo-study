import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())
G = [[] for _ in range(n + 1)]
v = [False] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


dp = [[0, 0] for _ in range(n + 1)]

def dfs(start):
    v[start] = True
    dp[start][0] = 0
    dp[start][1] = 1

    for i in G[start]:
        if not v[i]:
            dfs(i)
            dp[start][0] += dp[i][1]
            dp[start][1] += min(dp[i][0], dp[i][1])

dfs(1)
print(min(dp[1][0], dp[1][1]))
