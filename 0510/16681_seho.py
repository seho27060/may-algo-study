# 2 ~ n-1 개의 임의 등산목표
# 1 - 목적 - n(고려대)
# 아.. 이동 마다 성취를 얻는게 아니라, 해당 지점에 도착하면 그때 한번 성취감을 얻음.
# 답이 음수 or 갈수 없다면 Impossible
# 아니라면 최대값 출력.
# 200000*100000
import sys
from heapq import *

input = sys.stdin.readline
INF = float('inf')

def djk(start):
    global n, heights, nodes, d, e
    visited = [INF]*(n+1)
    visited[start] = 0

    queue = []
    heappush(queue,[visited[start],start])
    while queue:
        cost, now = heappop(queue)
        if visited[now] < cost:
            continue
        for node in nodes[now]:
            nxt, nxtCost = node
            if heights[nxt] > heights[now] and visited[nxt] > cost + nxtCost:
                visited[nxt] = cost + nxtCost
                heappush(queue,[visited[nxt],nxt])

    return visited

n, m, d, e = map(int,input().split())
# 노드개수, 간선개수, 거리당 체력소모, 높이당 성취획득
heights = [0]
heights.extend(list(map(int,input().split()))) #

nodes = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, w = map(int,input().split())
    nodes[start].append([end,w])
    nodes[end].append([start,w])
## 높이증가하는 djk
## 높이 감소하는 djk

dst1 = djk(1) # 1에서 정방향
# print(dst1)
dst2 = djk(n) # n에서 정방향(목표에서 내리막길이 됨)
# print(dst2)
answer = -INF
for target in range(2,n):
    if dst1[target] < INF and dst2[target] < INF:
        if answer < e*heights[target] - d*(dst1[target] + dst2[target]):
            answer = e*heights[target] - d*(dst1[target] + dst2[target])
if -INF < answer < INF:
    print(answer)
else:
    print("Impossible")
