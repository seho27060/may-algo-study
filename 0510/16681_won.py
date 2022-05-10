import sys
input = sys.stdin.readline
from heapq import heappush, heappop


def f(s):
    arr = [INF] * (N + 1)
    qu = []
    qu.append((0, s))
    arr[s] = 0
    while qu:
        curD, curN = heappop(qu)

        if arr[curN] < curD:
            continue

        for newN, newD in G[curN]:
            if h[curN] >= h[newN]:
                continue
            if arr[newN] > curD + newD:
                arr[newN] = curD + newD
                heappush(qu, (curD + newD, newN))

    return arr

N, M, D, E = map(int, input().split())
h = [0] + list(map(int, input().split()))
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, n = map(int, input().split())
    G[a].append((b, n))
    G[b].append((a, n))

INF = 999999999999999999999
ans = -INF

dist1Arr = f(1)
distNArr = f(N)

for target in range(2, N):
    achievement = h[target] * E
    totalDist = dist1Arr[target] + distNArr[target]
    consumedHealth = totalDist * D
    result = achievement - consumedHealth
    ans = max(ans, result)

if ans == -INF:
    ans = 'Impossible'
print(ans)
