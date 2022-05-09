import sys
input = sys.stdin.readline
from heapq import heappush, heappop


def f(s):
    qu = []
    qu.append((0, s))
    distArr[s] = 0
    while qu:
        curDist, curN = heappop(qu)

        if distArr[curN] < curDist:
            continue

        for newN, newDist in G[curN]:
            if distArr[newN] > curDist + newDist:
                distArr[newN] = curDist + newDist
                heappush(qu, (curDist + newDist, newN))
                p[newN] = curN

V, E, P = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))
INF = 50000001
p = [0] * (V + 1)
distArr = [INF] * (V + 1)
f(1)
result1 = distArr[V]

result2 = distArr[P]

distArr = [INF] * (V + 1)
f(P)
result3 = distArr[V]
if result1 == result2 + result3:
    print('SAVE HIM')
else:
    print('GOOD BYE')