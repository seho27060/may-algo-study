import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 0] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

def dfs(x):
    visited[x] = 1
    dp[x][0] = 1
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            dp[x][0] += min(dp[i][0], dp[i][1])
            dp[x][1] += dp[i][0]

dfs(1)
print(min(dp[1][0], dp[1][1]))