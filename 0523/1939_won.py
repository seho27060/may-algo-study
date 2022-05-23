import sys
input = sys.stdin.readline
from collections import deque

def f(mid):
    qu = deque()
    qu.append(S)
    visited[S] = 1
    while qu:
        t = qu.popleft()
        if t == E:
            return True
        for newN, newW in G[t]:
            if mid <= newW and visited[newN] == 0:
                qu.append(newN)
                visited[newN] = 1
    return False

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((B, C))
    G[B].append((A, C))

S, E = map(int, input().split())


sm, lg = 1, 1000000000
while sm <= lg:
    visited = [0] * (N + 1)
    mid = (sm + lg) // 2
    if f(mid):
        sm = mid + 1
    else:
        lg = mid - 1
print(lg)
