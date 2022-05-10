
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize  # 1e10도 초과하는 범위의 수가 나온다


def dijkstra(start):
    Q = [(0, start)]
    dist = [INF for _ in range(N + 1)]
    dist[start] = 0
    visit = set()

    while Q:
        cost, curV = heappop(Q)
        if curV in visit: continue
        visit.add(curV)

        for neiCost, neiV in adj[curV]:
            if neiV not in visit:
                if heights[neiV] > heights[curV] and dist[neiV] > cost + neiCost:
                    heappush(Q, (cost + neiCost, neiV))
                    dist[neiV] = cost + neiCost

    return dist


N, M, D, E = map(int, input().split())
heights = [0] + list(map(int, input().split()))
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, n = map(int, input().split())
    adj[a].append((n, b))
    adj[b].append((n, a))

# 다 탐색할 필요 없다. 어차피 D로 기록할 수 있기 때문에
# 대신 편의상 둘다 오르막길 버전으로 하기 위해
# 내리막길은 반대로 끝에서부터 출발하는 것으로 한다 (양방향이라 쉽게 가능)
to_target = dijkstra(1)
to_korea = dijkstra(N)

ans = -INF
for i in range(2, N):
    if to_target[i] == INF or to_korea[i] == INF: continue
    tmp = E * heights[i] - (to_target[i] + to_korea[i]) * D
    if ans < tmp:
        ans = tmp

if ans != -INF: print(ans)
else: print("Impossible")


'''
4 3 4 10
1 2 3 4
1 2 1
2 3 2
3 4 3

2 1 4 10
3 3
1 2 3
'''