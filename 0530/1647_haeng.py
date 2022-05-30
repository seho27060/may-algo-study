import heapq
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
road = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int, input().split())
    road[a].append((c,b))
    road[b].append((c,a))

visited=[0]*(N+1)
ST=[]
ST2 = []      #사용하는 길 유지비기록
result=0
visited[1]=1
for i in road[1]:
    heapq.heappush(ST, i)

while ST:
    cnt, next = heapq.heappop(ST)
    if visited[next]:
        continue
    visited[next] = 1
    ST2.append(cnt)
    result += cnt

    for C,N in road[next]:
        if visited[N]: continue
        heapq.heappush(ST,(C,N))


print(result-max(ST2))