import heapq

def dijk(start):
    result = [1000001] * (N + 1)
    result[start] = 0
    ST = [[0, start]]
    while ST:
        cnt,now = heapq.heappop(ST)

        if cnt > result[now]:
            continue

        for i in road[now]:
            if result[i[0]] > cnt + i[1]:
                result[i[0]] = cnt + i[1]
                heapq.heappush(ST,(cnt+i[1],i[0]))
    return result



N,M,X = map(int,input().split())
road= [[] for _ in range(N+1)]
for _ in range(M):
    A,B,C = map(int, input().split())
    road[A].append([B,C])


go = dijk(X)
Y = 0
for i in range(1,N+1):
    if i==X: continue
    if Y < go[i] + dijk(i)[X]:
        Y = go[i] + dijk(i)[X]
print(Y)
