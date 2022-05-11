import heapq
def dijk(start):
    d = [inf] * (N + 1)
    d[start] = 0
    q = []
    heapq.heappush(q, (d[start], start))
    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        for j in G[now]:
            cost = dist + j[1]
            if height[now] >= height[j[0]]:
                continue
            if d[j[0]] > cost:
                d[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))
    return d

N, M, D, E = map(int, input().split())
height = [0] + list(map(int, input().split()))
G = [[] for _ in range(N+1)]

inf = 1012345678908765432
max_sol = -inf
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))
top = dijk(1)
goal = dijk(N)

for i in range(2, N):
    if top[i] != -inf and goal[i] != -inf:
        up = height[i] * E
        total = top[i] + goal[i]
        ans = up - (total * D)
        if max_sol < ans:
            max_sol = ans
if max_sol == -inf:
    print('Impossible')
else:
    print(max_sol)