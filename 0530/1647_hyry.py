import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def prim():
    Q = [(0, 1)]
    visit = [False] * (V + 1)
    cnt = 0

    ans = maxV = 0
    while cnt < V:
        cost, curV = heappop(Q)
        if visit[curV]: continue
        visit[curV] = True
        cnt += 1
        ans += cost
        if maxV < cost:
            maxV = cost

        for neiCost, neiV in adj[curV]:
            if not visit[neiV]:
                heappush(Q, (neiCost, neiV))

    return ans - maxV


V, E = map(int, input().split())
adj = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    adj[A].append((C, B))
    adj[B].append((C, A))

print(prim())