from heapq import *
import sys
input = sys.stdin.readline
INF = sys.maxsize
def prim():
    D[1] = 0
    Q = [(0, 1)]
    while Q:
        weight, n1 = heappop(Q)
        V[n1] = True

        for c, n2 in G[n1]:
            if not V[n2] and c < D[n2]:
                D[n2] = c
                heappush(Q, (c, n2))

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((C, B))
    G[B].append((C, A))

D = [INF] * (N+1)
D[0] = 0
V = [False] * (N+1)
prim()
print(sum(D) - max(D))