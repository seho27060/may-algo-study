

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)


def dfs(parent):
    memo[parent][1] = popul[parent]
    visit[parent] = True

    for child in adj[parent]:
        if not visit[child]:
            dfs(child)
            memo[parent][0] += max(memo[child][0], memo[child][1])
            memo[parent][1] += memo[child][0]


N = int(input())
popul = [0] + list(map(int, input().split()))

adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

visit = [False] * (N + 1)
memo = [[0, 0] for _ in range(N + 1)]
dfs(1)
print(max(memo[1][0], memo[1][1]))
