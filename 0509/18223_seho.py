# 1 -> p -> v 로 가는데. 1->v 이 최소거리와 같거나 작다면 SAVE HIM
# 아니라면 GOOD BYE
import sys
from heapq import *
input = sys.stdin.readline
INF = sys.maxsize
# 양방향, 중복간선없음, 자기자신 없음 => adj array
def djk(start):
    global nodes, v
    dst = [INF]*(v+1)
    dst[start] = 0

    queue = []
    heappush(queue, [0,start])

    while queue:
        cost, now = heappop(queue)
        for node in nodes[now]:
            nxt, nxtCost = node
            if dst[nxt] > cost + nxtCost:
                dst[nxt] = cost + nxtCost
                heappush(queue,[dst[nxt],nxt])
    return dst

v, e, p = map(int,input().split())
nodes = [[] for _ in range(v+1)]

for _ in range(e):
    s, e, w = map(int,input().split())
    nodes[s].append([e,w])
    nodes[e].append([s,w])
# 1 ~ v djk 구하고
# 1 ~ p, p ~ v djk 구하자
startToEnd = djk(1)
pToEnd = djk(p)
if startToEnd[p] + pToEnd[v] <= startToEnd[v]:
    print("SAVE HIM")
else:
    print("GOOD BYE")