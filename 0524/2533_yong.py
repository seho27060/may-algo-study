import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
# 트리의DP를 적용하는문제
# 각 노드가 얼리어답터인 경우와 아닌 경우를 판단해 답을 구하는 방식
def dfs(u):
    visited[u] = 1
    DP[u][1] = 1
    for i in G[u]:
        if not visited[i]:
            dfs(i)
            DP[u][1] += min(DP[i][0],DP[i][1])
            DP[u][0] += DP[i][1]

N = int(input())
visited = [0] * (N+1)
DP = [ [0,0] for _ in range(N+1) ]
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
dfs(1)
print(min(DP[1]))