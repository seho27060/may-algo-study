from collections import defaultdict
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((C, B))

D = [INF] * (N+1)
D[1] = 0
for i in range(N):
    for n1 in range(1, N+1):
        if D[n1] == INF:
            continue
        for t, n2 in G[n1]:
            if D[n1] + t < D[n2]:
                D[n2] = D[n1] + t
                if i == N-1:
                    print(-1)
                    exit(0)

for i in range(2, N+1):
    if D[i] == INF:
        print(-1)
    else:
        print(D[i])
