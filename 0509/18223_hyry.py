import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def dijkstra(start, end):
    global minCost, friendCost
    Q = [(0, start)]
    visit = set()

    while Q:
        cost, curV = heappop(Q)
        if curV in visit: continue
        if curV == end: return cost

        visit.add(curV)

        for neiCost, neiV in adj[curV]:
            if neiV not in visit:
                heappush(Q, (cost + neiCost, neiV))



V, E, P = map(int, input().split())
adj = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))

toFriend, withFriend = dijkstra(1, P), dijkstra(P, V)
minRoute = dijkstra(1, V)


if minRoute < toFriend + withFriend:
    print("GOOD BYE")
else:
    print("SAVE HIM")
