import sys
from heapq import *
input = sys.stdin.readline
INF = sys.maxsize

def shot(x, y, nx, ny): # 대포 타고 이동하는 경우
    d = ((x-nx) ** 2 + (y-ny) ** 2) ** 0.5
    t = abs(50 - d) / 5
    return 2 + t

def walk(x, y, nx, ny): # 걸어서 이동하는 경우
    d = (((x-nx) ** 2 + (y-ny) ** 2) ** 0.5)
    t = d / 5
    return t

pX, pY = map(float, input().split())
dX, dY = map(float, input().split())

n = int(input())
G = [[dX, dY]]
for _ in range(n):
    G.append(list(map(float, input().split())))

D = [INF] * (n+1)
Q = []
for i in range(n+1): # 일단 시작점에서는 대포 or 목적지까지 걸어가야하므로 walk로 D 테이블 초기화
    nx, ny = G[i]
    D[i] = walk(pX, pY, nx, ny)
    heappush(Q, (D[i], nx, ny, i))

while Q:
    t, x, y, n1 = heappop(Q)

    if D[n1] < t:
        continue

    for n2, axis in enumerate(G):
        nx, ny = axis
        ct = shot(x, y, nx, ny)
        if t + ct < D[n2]:
            D[n2] = t + ct
            heappush(Q, (D[n2], nx, ny, n2))

        ct = walk(x, y, nx, ny)
        if t + ct < D[n2]:
            D[n2] = t + ct
            heappush(Q, (D[n2], nx, ny, n2))

print(D[0])
