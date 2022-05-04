
import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def dijkstra(adj, dist):
    Q = [(0, X)]
    dist[X] = 0
    visit = set()

    while Q:
        cost, curV = heappop(Q)
        if curV in visit: continue
        visit.add(curV)

        for neiCost, neiV in adj[curV]:
            if neiV not in visit and dist[neiV] > cost + neiCost:
                dist[neiV] = cost + neiCost
                heappush(Q, (cost + neiCost, neiV))


N, M, X = map(int, input().split())
goAdj = [[] for _ in range(N + 1)]
backAdj = [[] for _ in range(N + 1)]
goDist = [1e10] * (N + 1)
backDist = [1e10] * (N + 1)
for _ in range(M):
    v1, v2, w = map(int, input().split())
    goAdj[v2].append((w, v1))
    backAdj[v1].append((w, v2))

dijkstra(goAdj, goDist)
dijkstra(backAdj, backDist)

longest = 0
for i in range(1, N + 1):
    if longest < goDist[i] + backDist[i]:
        longest = goDist[i] + backDist[i]

print(longest)
