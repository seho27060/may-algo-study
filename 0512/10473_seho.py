### 220512 10473 인간대포
# 달린다면? 5미터당 1초/ 대포탄다면? 원하는 방향으로 50m 2초컷
# 현재위치에서 목적지로 최대한 빨리가는 경로의 시간?
# 대포가 노드, 이동은 항상 노드를 향해야한다.
# n은 50000? 0.01 ~ 500.00 의 실수. 소수점아래 2자리까지니까.
import sys
from heapq import *
input = sys.stdin.readline
INF = sys.maxsize

def dst(start,target):
    nowX, nowY = start
    nxtX, nxtY = target
    nxtDst = ((nowX-nxtX)**2+(nowY-nxtY)**2)**(0.5)
    if nxtDst > 50:
        nxtCost = 2 + (nxtDst-50)/5
    elif nxtDst == 50:
        nxtCost = 2
    else:
        nxtCost = min((nxtDst)/5,2+(50-nxtDst)/5)
    return nxtCost

def djk(startX,startY):
    global n, nodes
    nodes[f"{startX},{startY}"] = 0

    for now in list(nodes.keys())[1:]:
        nowX, nowY = map(float,now.split(','))
        nodes[now] = (((startX-nowX)**2+(startY-nowY)**2)**(0.5))/5

    for _ in range(len(nodes)):

        for now ,cost in list(nodes.items())[1:]:
            [nowX,nowY] = map(float,now.split(','))
            for nxt in nodes.keys():
                nxtX,nxtY = map(float,nxt.split(','))
                if nowX != nxtX and nowY != nxtY:
                    nxtCost = dst([nowX,nowY],[nxtX,nxtY])
                    if nodes[nxt] == -1 or nodes[nxt] > cost+nxtCost:
                        nodes[nxt] = cost+nxtCost

startX, startY = map(float,input().split())
goalX, goalY = map(float,input().split())

n = int(input())
nodes = {}
nodes[f"{startX},{startY}"] = -1
nodes[f"{goalX},{goalY}"] = -1
for _ in range(n):
    x,y = map(float,input().split())
    nodes[f"{x},{y}"] = -1

djk(startX,startY)
print(nodes[f"{goalX},{goalY}"])