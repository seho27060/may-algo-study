import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def f(c):
    visited[c] = 1
    dp[c][0] = people[c]
    for n in G[c]:
        if visited[n] == 0:
            f(n)
            dp[c][0] += dp[n][1]
            dp[c][1] += max(dp[n][0], dp[n][1])

N = int(input())

people = [0] + list(map(int, input().split()))
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [0] * (N + 1)
dp = [[0, 0] for _ in range(N + 1)]
f(1)
print(max(dp[1][0], dp[1][1]))
