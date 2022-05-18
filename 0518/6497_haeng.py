from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

while 1:
    m,n = map(int,input().split())
    if m==0 and n ==0:
        break
    road=defaultdict(list)
    Y=0
    for _ in range(n):
        a,b,c = map(int,input().split())
        Y += c
        road[a].append((c,b))
        road[b].append((c,a))

    ST = [0]
    route = []
    for i in road[0]:
        heapq.heappush(route,i)

    result = 0
    while route:
        cnt, next = heapq.heappop(route)
        if next in ST:
            continue
        result += cnt
        ST.append(next)

        for C, N in road[next]:
            if N in ST: continue
            heapq.heappush(route, (C, N))

    print(Y-result)