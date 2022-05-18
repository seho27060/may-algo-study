### 220518 6497 전력난
import sys
from heapq import *

input = sys.stdin.readline
INF = float('inf')

def mst():
    global m, n, nodes, allpath

    dst = []

    vertices = [0]*m
    vertices[0] = 1

    queue = nodes[0]
    heapify(queue)

    while queue:
        cost, s, e = heappop(queue)

        if vertices[e] == 0:
            vertices[e] = 1
            dst.append([cost,s,e])

            for node in nodes[e]:
                if vertices[node[2]] == 0:
                    heappush(queue,node)
    for d in dst:
        allpath -= d[0]
    print(allpath)
while 1:
    m, n = map(int,input().split()) #집의 개수, 길의 개수
    if m == 0 and n == 0:
        break

    nodes = [[] for _ in range(m)]
    allpath = 0
    for _ in range(n):
        x, y, z = map(int, input().split()) # 양방향도로
        nodes[x].append([z,x,y])
        nodes[y].append([z,y,x])
        allpath += z

    mst()
