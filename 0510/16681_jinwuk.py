from collections import deque
import sys, heapq

def func(start):
    visited=[INF]*(N+1)
    q= []
    heapq.heappush(q,[start,0])
    visited[0] =0
    visited[start] = 0
    while q:
        point,cnt = heapq.heappop(q)

        if visited[point] < cnt:
            continue

        for po,nu in lst[point]:
            if H[point] < H[po]:
                cost = cnt + nu
                if cost <visited[po]:
                    visited[po] = cost
                    heapq.heappush(q,[po,cost])
    return visited

INF=sys.maxsize
N,M,D,E = map(int,input().split()) #지점개수,경로개수,체력소모량, 높이성취감
H = [0] +list(map(int,input().split()))
lst = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    lst[a].append([b,c])
    lst[b].append([a,c])

home = func(1)
go = func(N)
result= []
for j in range(1,N+1):
    if home[j] != INF and go[j] != INF:
        result.append(H[j] * E - D*(home[j] + go[j]))

if result:
    print(max(result))
else:
    print("Impossible")
