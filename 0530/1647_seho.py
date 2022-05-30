#220530 1647 도시 분할 계획
# 양방향/ 최소스패닝/
# 최소스패닝 트리 만들고, 가장 비용이 큰 길을 지우면?

import sys
from heapq import *
input = sys.stdin.readline

def mst():
    global graphs,n
    dst = []
    vertices = [0]*(n+1)
    vertices[0] = 1
    vertices[1] = 1

    queue = graphs[1]
    heapify(queue)

    while queue:
        cost , now, nxt = heappop(queue)
        if vertices[nxt] == 0:
            vertices[nxt] = 1
            dst.append(cost)
            if len(dst) == n-1:
                break
            for graph in graphs[nxt]:
                if vertices[graph[2]] == 0:
                    heappush(queue,graph)
    output = sum(dst)-max(dst)
    return output

n, m = map(int,input().split())
graphs = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int,input().split())
    graphs[s].append([w, s, e])
    graphs[e].append([w, e, s])
result = mst()
print(result)

