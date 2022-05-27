import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(parent, weight):
    memo[parent] = weight
    visit[parent] = True

    for child, w in adj[parent]:
        if not visit[child]:
            dfs(child, w)
            memo[parent] += max(0, memo[child])


N = int(input())
adj = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    t, a, p = input().split()
    a, p = int(a), int(p)
    if t == 'W':
        a = -a

    adj[i].append((p, a))
    adj[p].append((i, a))

memo = [0] * (N + 1)
visit = [False] * (N + 1)
dfs(1, 0)
print(max(memo[1], 0))