
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra():
    Q = [(-INF, S)]
    visit = set()

    ans = INF
    while Q:
        weight, curV = heappop(Q)
        if curV in visit: continue
        ans = min(ans, -weight)
        if curV == G: return ans
        visit.add(curV)

        for neiCost, neiV in edges[curV]:
            if neiV not in visit:
                heappush(Q, (neiCost, neiV))

    return ans


N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    edges[A].append((-C, B))
    edges[B].append((-C, A))
S, G = map(int, input().split())

print(dijkstra())

