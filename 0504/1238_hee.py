from collections import defaultdict
import sys
from heapq import *
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(S, E):
    D = [INF] * (N+1)
    Q = [(0, S)]
    D[S] = 0
    while Q:
        c, n1 = heappop(Q)
        for cost, n2 in G[n1]:
            if cost + c < D[n2]:
                D[n2] = cost + c
                heappush(Q, (cost + c, n2))
    return D[E]

N, M, X = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    A, B, T = map(int, input().split())
    G[A].append((T, B))

ans = 0
for i in range(1, N+1):
    val = dijkstra(i, X) + dijkstra(X, i)
    ans = max(ans, val)
print(ans)


