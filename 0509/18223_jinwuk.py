from collections import deque
import sys

def func(start,end):
    visited = [INF] * (V + 1)
    q = deque()
    q.append([start,0])
    visited[start] =0
    while q:
        point,cnt = q.popleft()

        for po,nu in lst[point]:
            cost = cnt +nu
            if cost < visited[po]:
                visited[po] = cost
                q.append([po,cost])
    return visited[end]

INF = sys.maxsize
V,E,P =map(int,input().split())
lst = [[] for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    lst[a].append([b,c])
    lst[b].append([a,c])

friend = func(1,P) + func(P,V)
solo = func(1,V)

if friend <= solo:
    print("SAVE HIM")
else:
    print("GOOD BYE")