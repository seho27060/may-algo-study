import sys
from collections import deque
input = sys.stdin.readline
# bfs와 이분탐색 활용문제
# 처음에는 다리무게를 활용하여 도착지에 갈 수 있는 최소 무게를 탐색
# 나중에는 이분탐색을 활용해 도달할 수 있는 무게의 최대값을 탐색

def bfs(w):
    q = deque()
    q.append(S)
    visited = [0] * (N+1)
    visited[S] = 1
    while q:
        A = q.popleft()
        for B, C in G[A]:
            if not visited[B] and w <= C:
                visited[B] = 1
                q.append(B)
    if visited[E]:
        return True
    return False
    

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((B, C))
    G[B].append((A, C))
S, E = map(int, input().split())
minW = 1
maxW = 1000000000
ans = 0
while minW <= maxW:
    midW = (maxW + minW) // 2
    if bfs(midW):
        ans = midW
        minW = midW + 1
    else:
        maxW = midW - 1
print(ans)