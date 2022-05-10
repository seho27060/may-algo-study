import sys
from heapq import *
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize

def dijk(S):
    dijk = [INF] * (N + 1)
    Q = [(0, S)]
    dijk[S] = 0
    while Q:
        c, n1 = heappop(Q)

        if dijk[n1] < c:
            continue

        for d, n2 in G[n1]:
            if H[n1] < H[n2] and dijk[n2] > c + D * d:
                dijk[n2] = c + D * d
                heappush(Q, (dijk[n2], n2))
    return dijk

N, M, D, E = map(int, input().split())
H = [0] + list(map(int, input().split()))
G = defaultdict(list)
for _ in range(M):
    a, b, n = map(int, input().split())
    G[a].append((n, b))
    G[b].append((n, a))

ans = -INF
D1 = dijk(1)
D2 = dijk(N)
for i in range(2, N):
    if D1[i] == INF or D2[i] == INF:
        continue
    ans = max(ans, -D1[i] + H[i] * E - D2[i])

if ans == -INF:
    print("Impossible")
else:
    print(ans)

