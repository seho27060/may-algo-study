import heapq
import collections
import sys
input = sys.stdin.readline

n, m, x = map(int, input().split())

graph_go = collections.defaultdict(list)
graph_back = collections.defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph_go[u].append((v, w))
    graph_back[v].append((u, w))

def dijkstra(graph):
    dist = [1e9] * (n+1)
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

dist_go = dijkstra(graph_go)
dist_back = dijkstra(graph_back)

sum_dist = [x+y for x, y in zip(dist_go[1:], dist_back[1:])]
print(max(sum_dist))