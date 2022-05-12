
import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def dijkstra():
    Q = [(0, sX, sY)]
    visit = set()

    while Q:
        cost, curX, curY = heappop(Q)
        if (curX, curY) in visit: continue
        if curX == gX and curY == gY: return cost
        visit.add((curX, curY))

        for (neiX, neiY) in V:
            if (neiX, neiY) != (curX, curY) and (neiX, neiY) not in visit:
                # 대포가 아닌 경우
                dist = (abs(curX - neiX) ** 2 + abs(curY - neiY) ** 2) ** 0.5
                heappush(Q, (cost + dist / 5, neiX, neiY))
                # 대포인 경우
                if (curX, curY) != (sX, sY):
                    if dist == 50:
                        tmp = cost + 2
                    elif dist > 50:
                        tmp = cost + 2 + (dist - 50) / 5
                    else:
                        tmp = cost + 2 + (50 - dist) / 5
                    heappush(Q, (tmp, neiX, neiY))


V = []
sX, sY = map(float, input().split())
gX, gY = map(float, input().split())
V.append((gX, gY))
n = int(input())
for _ in range(n):
    x, y = map(float, input().split())
    V.append((x, y))

print(dijkstra())
