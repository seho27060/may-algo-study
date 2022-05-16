
import sys
input = sys.stdin.readline
INF = sys.maxsize


def bellmanFord():
    global dist
    dist[1] = 0

    for _ in range(N - 1):
        tmp = dist.copy()

        for start, end, cost in edges:
            if tmp[start] == INF: continue
            if tmp[end] > dist[start] + cost:
                tmp[end] = dist[start] + cost

        dist = tmp

    for a, b, c in edges:
        if dist[a] == INF: continue
        if dist[b] > dist[a] + c:
            return False

    return True


N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

dist = [INF for _ in range(N + 1)]

if bellmanFord():
    for i in range(2, len(dist)):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
else:
    print(-1)