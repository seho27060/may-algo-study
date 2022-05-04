import heapq
def dijk(start):
    d = [inf] * (n + 1)
    q = []
    d[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        for j in G[now]:
            cost = dist + j[1]
            if cost < d[j[0]]:
                d[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))
    return d
n, m, h = map(int, input().split())
inf = 1e9
max_sol = -1
G = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
hd = dijk(h)

for i in range(1, n+1):
    ans = dijk(i)[h]

    sol = ans + hd[i]
    if sol > max_sol:
        max_sol = sol
print(max_sol)