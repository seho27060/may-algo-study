import heapq
import sys
input = sys.stdin.readline
# 다익스트라를 통해 각 노드로 이동하는 최단거리를 구함
# 방문배열을 생성하여 각 노드를 방문하는 최단거리를 갖는 노드번호를 저장

def dijk():
    D = [1000000000] * (N+1)
    D[1] = 0
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        dis, now = heapq.heappop(q)
        if D[now] < dis:
            continue
        for e, c in G[now]:
            if D[e] > dis + c:
                D[e] = dis + c
                visited[e] = now
                heapq.heappush(q, (dis+c, e))

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((B, C))
    G[B].append((A, C))
dijk()
print(len(visited) - visited.count(0))
for i in range(2, N+1):
    print(i, visited[i])