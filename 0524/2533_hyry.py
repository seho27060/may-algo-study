

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(parent):
    visit[parent] = True
    memo[parent][1] = 1  # 자기 자신을 포함하는 경우

    for child in adj[parent]:
        if not visit[child]:
            dfs(child)  # leaf 먼저 해야 하니 끝까지 갔다 나오면서 하는 구도로
            memo[parent][1] += min(memo[child][0], memo[child][1])  # 그래서 memo가 dfs보다 아래에 위치
            memo[parent][0] += memo[child][1]


N = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visit = [False] * (N + 1)
memo = [[0, 0] for _ in range(N + 1)]

dfs(1)
print(min(memo[1][0], memo[1][1]))
