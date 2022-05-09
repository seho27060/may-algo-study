from collections import defaultdict
import sys
from heapq import *
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(S,E):
    D = [INF] * (V + 1)
    D[S] = 0
    Q = [(0, S)]
    while Q:
        c, n1 = heappop(Q)

        if D[n1] < c:
            continue

        for cost, n2 in G[n1]:
            if c + cost < D[n2]:
                D[n2] = c + cost
                heappush(Q, (D[n2], n2))
    return D


V, E, P = map(int, input().split())
G = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    G[a].append((c, b))
    G[b].append((c, a))

D1 = dijkstra(1, V)
D2 = dijkstra(P, V)

if D1[V] == D1[P] + D2[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")
