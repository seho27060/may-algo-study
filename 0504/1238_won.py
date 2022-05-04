import sys
input = sys.stdin.readline
from heapq import heappush, heappop


INF = 100001
N, M, X = map(int, input().split())
backG = [[] for _ in range(N + 1)]
goG = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    backG[a].append((b, t))
    goG[b].append((a, t))

def f(s, G):
    arr = [INF] * (N + 1)
    qu = []
    qu.append((0, s))
    arr[s] = 0
    while qu:
        curTime, curN = heappop(qu)

        if arr[curN] < curTime:
            continue

        for newN, newTime in G[curN]:
            if arr[newN] > curTime + newTime:
                arr[newN] = curTime + newTime
                heappush(qu, (curTime + newTime, newN))
    return arr
goArr = f(X, goG)
backArr = f(X, backG)
ans = 0

for i in range(1, N + 1):
    ans = max(ans, goArr[i] + backArr[i])

print(ans)
