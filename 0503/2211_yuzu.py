import heapq
import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra():
    cnt = 0
    ans = [0]*(n+1)
    net = [1e9] * (n+1)
    net[1] = 0
    q = [(0, 1)]
    while q:
        d, node = heapq.heappop(q)
        if net[node] < d:
            continue
        for v, w in graph[node]:
            if d+w < net[v]:
                net[v] = d+w
                # 선을 새로 생성하는 경우만 cnt += 1 선을 옮기는 경우는 더해주지 않음
                if ans[v] == 0:
                    cnt += 1
                # 두 노드 사이의 거리가 최단 거리 일때 갱신
                ans[v] = node
                heapq.heappush(q, (d+w, v))
    print(cnt)
    for i in range(2, cnt+2):
        print(ans[i], i)
    return

dijkstra()