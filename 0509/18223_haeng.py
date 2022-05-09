import heapq

def find(start,end):
    result = [100000001] * (V+1)
    result[start] = 0
    ST = [[0,start]]

    while ST:
        cnt,now = heapq.heappop(ST)

        for i in road[now]:
            if result[i[0]] > cnt + i[1]:
                result[i[0]] = cnt+i[1]
                heapq.heappush(ST,(cnt+i[1],i[0]))

    return result[end]


V,E,P = map(int,input().split())
road=[[] for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    road[a].append([b,c])
    road[b].append([a,c])

R1 = find(1,V)
R2 = find(1,P) + find(P,V)

if R1 == R2:
    print('SAVE HIM')
else:
    print('GOOD BYE')