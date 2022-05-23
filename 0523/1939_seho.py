#220523 1939 중량제한
import sys
from heapq import *
input = sys.stdin.readline
INF = sys.maxsize

def djk():
    global n, graphs, start, end
    visited = [1]*(n+1)
    visited[start] = -INF

    queue = []
    heappush(queue,[-INF,start])

    while queue:
        cost, now = heappop(queue)
        if now == end:
            print(-cost)
            return
        for nxt, nxtCost in graphs[now]:
            comp = max(nxtCost,cost)
            if visited[nxt] == 1 or visited[nxt] > comp:
                visited[nxt] = comp
                heappush(queue,[comp,nxt])
    print(-visited[end])
    return

n, m = map(int,input().split())
graphs = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int,input().split())
    graphs[s].append([e, -w])
    graphs[e].append([s, -w])
start, end = map(int,input().split())
# print(graphs)
djk()