from collections import defaultdict
import sys
input = sys.stdin.readline
INF = sys.maxsize

def bf():
    D[1] = 0
    for i in range(1, n+1):
        for n1 in range(1, n+1):
            if D[n1] == -INF:
                continue
            for w, n2 in G[n1]:
                if D[n1] + w > D[n2]:
                    D[n2] = D[n1] + w
                    V[n2] = n1
                    if i == n:
                        D[n2] = INF

n, m = map(int, input().split())
G = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    G[u].append((w, v))

D = [-INF] * (n+1)
V = [0] * (n+1)
bf()

i = n
ans = [n]
while i != 1:
    if D[i] != INF:
        ans.append(V[i])
    else:
        print(-1)
        exit(0)
    i = V[i]
print(*ans[::-1])