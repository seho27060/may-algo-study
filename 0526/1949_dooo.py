import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def dfs(start):
    v[start] = 1
    dp[start][0] = p[start]
    for i in G[start]:
        if v[i] == 0:
            dfs(i)
            dp[start][0] += dp[i][1]
            dp[start][1] += max(dp[i][0], dp[i][1])



n = int(input())
p = [0] + list(map(int, input().split()))
G = [[] for _ in range(n+1)]

v = [0] * (n+1)
dp = [[0] * 2 for _ in range(n+1)]

for _ in range(n-1):
    a, b =map(int, input().split())
    G[a].append(b)
    G[b].append(a)
dfs(1)
print(max(dp[1][0], dp[1][1]))