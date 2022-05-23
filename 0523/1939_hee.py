from collections import defaultdict, deque
import sys
input = sys.stdin.readline
INF = 1_000_000_000

def bfs(val):
    V = [False] * (N+1)
    V[S] = True
    Q = deque([S])
    while Q:
        n1 = Q.popleft()

        if n1 == E:
            return True

        for w, n2 in G[n1]:
            if not V[n2] and val <= w:
                V[n2] = True
                Q.append(n2)
    return False

N, M = map(int,input().split())

G = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((C, B))
    G[B].append((C, A))
# 안 돼서 도전한 이분 탐색 풀이...


S, E = map(int, input().split())
low, high = 1, INF
while low <= high:
    mid = (high + low) // 2
    if bfs(mid):
        low = mid + 1
    else:
        high = mid - 1
print(high)

from collections import defaultdict
from heapq import *
import sys

input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())

G = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((C, B))
    G[B].append((C, A))

S, E = map(int, input().split())
V = [False] * (N+1)
V[S] = INF
Q = [(-INF, S)]
while Q:
    min_w, n1 = heappop(Q)

    if min_w > -V[n1]:
        continue

    for w, n2 in G[n1]:
        temp = min(-min_w, w)
        if not V[n2] or V[n2] < temp:
            V[n2] = temp
            heappush(Q, (-temp, n2))
print(V[E])
# 중간에 마이너스 하나 안 붙여서 시초났던 초반 풀이...