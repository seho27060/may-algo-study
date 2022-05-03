from heapq import *
from collections import defaultdict
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((C, B))
    G[B].append((C, A))

V = [False] * (N+1)
V[1] = True
Q = []
for cost, n2 in G[1]:
    heappush(Q, (cost, 1, n2))
ans = []

while Q:
    c, n1, n2 = heappop(Q)

    if V[n2]:
        continue
    ans.append((n1, n2))
    V[n2] = True

    for cost, n3 in G[n2]:
        if not V[n3]:
            heappush(Q, (c + cost, n2, n3))

print(len(ans))
for i in ans:
    print(*i)