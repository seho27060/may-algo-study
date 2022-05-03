import heapq

def dijk(X,start):
    X[start]=0
    ST=[[start,0]]

    while ST:
        now,cnt = heapq.heappop(ST)

        for i in road[now]:
            if X[i[0]] > cnt + i[1]:
                X[i[0]] = cnt + i[1]
                heapq.heappush(ST, (i[0], cnt+i[1]))
                Y[i[0]] = [now,i[0]]                    #갱신될경우 가장 마지막 경로만 기록
    return X



N,M = map(int,input().split())
road = [[] for _ in range(N+1)]

for _ in range(M):
    A,B,C = map(int, input().split())
    road[A].append([B,C])
    road[B].append([A,C])


result1 = [N * 10 + 1] * (N + 1)
Y = [[] for _ in range(N+1)]           #해당 컴퓨터의 통신경로중 가장 마지막 경로만 모아두면 최소 회선
dijk(result1,1)


print(N-1)     #복구할 최소 회선은 한 컴퓨터당 최소 1개는 필요하기에 결국 N-1개
for j in Y:
    if j:
        print(*j)

