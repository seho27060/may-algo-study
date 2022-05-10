import heapq
import collections
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m, d, e = map(int, input().split())
h = list(map(int, input().split()))
graph = collections.defaultdict(list)
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

def dijkstra(x):
    dist = [INF] * (n + 1)
    q = [(0, x)]
    dist[x] = 0
    while q:
        d, node = heapq.heappop(q)
        if dist[node] < d:
            continue
        for v, w in graph[node]:
            if h[v-1] > h[node-1]:
                if d+w < dist[v]:
                    dist[v] = d+w
                    heapq.heappush(q, (d+w, v))

    return dist

a = dijkstra(1)
b = dijkstra(n)
ans = -INF
for i in range(1, n+1):
    if a[i] != INF and b[i] != INF:
        if h[i-1]*e - d*(a[i]+b[i]) > ans:
            ans = h[i-1]*e - d*(a[i]+b[i])
print('Impossible') if ans == -INF else print(ans)