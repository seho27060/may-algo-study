import heapq


def dijk(start, end):
    d = [inf] * (n + 1)
    q = []
    d[start] = 0

    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if now == end:
            return d
        for j in G[now]:
            cost = d[now] + j[1]
            if d[j[0]] > cost:
                d[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))
    return d

n, m, p = map(int, input().split())
G = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

inf = 1e9



if (dijk(1,p)[p] + dijk(p,n)[n]) <= dijk(1, n)[n]:
    print('SAVE HIM')
else:
    print('GOOD BYE')