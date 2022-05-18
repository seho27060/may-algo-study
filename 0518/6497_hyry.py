
import sys
input = sys.stdin.readline
from heapq import heappop, heappush


def prim():
    Q = [(0, 0)]
    visit = set()

    ans = 0
    while len(visit) < n:
        curCost, curV = heappop(Q)
        if curV in visit: continue
        ans += curCost
        visit.add(curV)

        for neiCost, neiV in adj[curV]:
            if neiV not in visit:
                heappush(Q, (neiCost, neiV))

    return ans


while True:
    n, m = map(int, input().split())
    if n == m == 0: break
    adj = [[] for _ in range(n)]
    total = 0
    for _ in range(m):
        x, y, z = map(int, input().split())
        adj[x].append((z, y))
        adj[y].append((z, x))
        total += z


    print(total - prim())