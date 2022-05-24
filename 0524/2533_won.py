import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def f(n):
    dp[n][0] = 1
    visited[n] = 1
    for i in G[n]:
        if visited[i] == 0:
            f(i)
            # 얼리 어답터인 경우와 아닌 경우
            dp[n][0] += min(dp[i][0], dp[i][1])
            dp[n][1] += dp[i][0]

N = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

dp = [[0, 0] for _ in range(N + 1)]
visited = [0] * (N + 1)

f(1)
print(min(dp[1][0], dp[1][1]))
