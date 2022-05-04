from collections import deque
import sys
def func(start):
    global result
    q= deque()
    q.append([start,0])
    visited[start] = 0
    while q:
        point,cnt = q.popleft()
        if visited[point] < cnt:
            continue

        for po, nu in lst[point]:
            cost = cnt+nu
            if cost < visited[po]:
                visited[po] = cost
                q.append([po,cost])
    result.append(visited[X])

def funcc(s):
    global result
    q = deque()
    q.append([s, 0])
    visited[s] = 0
    while q:
        point, cnt = q.popleft()
        if visited[point] < cnt:
            continue

        for po, nu in lst[point]:
            cost = cnt + nu
            if cost < visited[po]:
                visited[po] = cost
                q.append([po, cost])
    for k in range(N+1):
        result[k]+=visited[k]

INF = sys.maxsize
N,M,X = map(int,input().split())
lst = [[] for _ in range(N+1)]
result =[0]
for i in range(M):
    a,b,c = map(int,input().split())
    lst[a].append([b,c])
for j in range(1,N+1):
    visited = [INF] * (N + 1)
    visited[0]=0
    func(j)
visited = [INF] * (N + 1)
visited[0]=0
funcc(X)
print(max(result))
