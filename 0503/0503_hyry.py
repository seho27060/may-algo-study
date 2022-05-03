
import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def dijkstra():
    Q = [(0, 1, 1)]  # cost, curV, preV
    D = [[i, 1e10] for i in range(N + 1)]
    visit = set()

    cnt = -1  # 맨 처음 시작점 제외
    ans = []
    while Q:
        cost, curV, preV = heappop(Q)
        if curV in visit: continue
        visit.add(curV)
        cnt += 1
        ans.append((preV, curV))

        for neiCost, neiV in adj[curV]:
            if D[neiV][1] > cost + neiCost:
                heappush(Q, (cost + neiCost, neiV, curV))
                D[neiV][0], D[neiV][1] = curV, cost + neiCost

    return cnt, ans


N, M = map(int, input().split())  # 1 ~ N
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    adj[A].append((C, B))
    adj[B].append((C, A))


cnt, ans = dijkstra()
print(cnt)
for a, b in ans:
    if a == b == 1: continue
    print(a, b)

'''
6 8
1 2 2
1 6 1
2 4 4
2 3 5
2 6 3
3 5 1
3 6 2
4 5 1

# 5
1 6
1 2
6 3
3 5
5 4

2 1
1 2 1
'''

