import heapq
import sys
input = sys.stdin.readline

def find(start):     #해당 위치까지 거리
    result = [9999999999999] * (N + 1)
    result[start] = 0
    ST = [(0, start)]
    while ST:
        hp, now = heapq.heappop(ST)

        if result[now] < hp:
            continue

        for j in road[now]:
            if Nlist[j[0]-1] <= Nlist[now-1]:
                continue
            if result[j[0]] > hp + j[1]:
                result[j[0]] = hp + j[1]
                heapq.heappush(ST, (hp + j[1], j[0]))
    return result


N,M,D,E = map(int, input().split())
Nlist=list(map(int,input().split()))
road=[[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    road[a].append((b,c))
    road[b].append((a,c))


#임의의 지점 선택
Y= -9999999999999

up = find(1)
down = find(N)
for i in range(2,N):
    if up[i] != 9999999999999 and down[i] != 9999999999999:
        if Y < Nlist[i-1]*E - (up[i]+down[i])*D:
            Y=Nlist[i-1]*E -(up[i]+down[i])*D

if Y == -9999999999999:
    print('Impossible')
else:
    print(Y)



