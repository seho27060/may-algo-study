import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
animal = [0, 0]

for i in range(2, n+1):
    u, v, w = input().split()
    graph[i].append(int(w))
    graph[int(w)].append(i)
    if u == 'S':
        animal.append(int(v))
    else:
        animal.append(-int(v))

dp = [0 for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

def dfs(x):
    visited[x] = 1
    dp[x] = animal[x]
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            if dp[i] >=0:
                dp[x] += dp[i]

dfs(1)
print(dp[1])