import sys
from collections import deque
def func():
    global result
    q= deque()
    q.append([1,0])
    visited[1]=0
    finish = INF
    while q:
        point,cnt = q.popleft()
        if visited[point] < cnt:
            continue

        for po, nu in lst[point]:
            cost = cnt + nu
            if cost < visited[po]:
                chk[po] =point
                visited[po] = cost
                q.append([po,cost])

INF = sys.maxsize
N, M = map(int,input().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    lst[a].append([b,c])
    lst[b].append([a,c])

chk = [0]*(N+1)
visited = [INF]*(N+1)
visited[0] = 0
result = []
func()

print(N-1)
for i in range(2, N+1):
    print(i, chk[i])