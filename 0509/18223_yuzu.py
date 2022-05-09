import heapq
import collections
import sys
input = sys.stdin.readline
inf = sys.maxsize

n, e, p = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(x):
    dist = [inf] * (n+1)
    q = [(0, x)]
    dist[x] = 0
    while q:
        d, node = heapq.heappop(q)
        if dist[node] < d:
            continue
        for v, w in graph[node]:
            if d+w < dist[v]:
                dist[v] = d+w
                heapq.heappush(q, (d+w, v))
    return dist

dist1 = dijkstra(1)
dist2 = dijkstra(p)

if dist1[-1]-dist1[p] == dist2[-1]:
    print('SAVE HIM')
else:
    print('GOOD BYE')