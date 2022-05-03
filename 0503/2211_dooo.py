import heapq
def dijk(start):
    q = []
    d[start][0] = 0
    heapq.heappush(q, (0, 1))
    while q:
        dist, now= heapq.heappop(q)
        for j in G[now]:
            cost = dist + j[1]
            if cost < d[j[0]][0]:
                d[j[0]][0] = cost
                d[j[0]][1] = now
                heapq.heappush(q, (cost, j[0]))

n, m = map(int, input().split())
inf = 1e9
G = [[] for _ in range(n+1)]
d = [[inf, 0] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))
dijk(1)
print(n-1)
for i in range(2, n+1):
    print(i, d[i][1])