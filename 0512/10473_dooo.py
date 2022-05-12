import heapq

inf = 1e9

def dijk(start):
    d[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        for j in G[now]:
            cost = d[now] + j[1]
            if d[j[0]] > cost:
                d[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


sx, sy = map(float, input().split())
ex, ey = map(float, input().split())
m = int(input())
arr = [(sx,sy)]
G =[[] for _ in range(m+2)]
d = [inf] * (m + 2)
for _ in range(m):
    x, y = map(float, input().split())
    arr.append((x, y))
arr.append((ex, ey))
for i in range(m+2):
    if i != 0:
        x, y = arr[i]
        val = ((sx-x)**2 + (sy-y)**2)**(1/2)
        G[0].append((i, val/5))

for i in range(1, m+1):
    for j in range(m+1):
        if i != j:
            cx, cy = arr[i]
            nx, ny = arr[j]
            val = ((cx-nx)**2 + (cy-ny)**2) **(1/2)
            if val>50:
                G[i].append((j, 2+(val-50)/5))

            else:
                G[i].append((j, 2+(50-val)/5))
for i in range(m+1):
    if i!=0:
        x, y = arr[i]
        val = ((ex-x)**2 + (ey-y)**2)**(1/2)

        if val>50:
            G[i].append((m+1, 2+(val-50)/5))
        else:
            G[i].append((m+1, 2+(50-val)/5))

dijk(0)

print(d[m+1])