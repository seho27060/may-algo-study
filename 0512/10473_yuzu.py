import heapq
import collections
import sys
input = sys.stdin.readline

sx, sy = map(float, input().split())
ex, ey = map(float, input().split())

def distance(a, b, c, d):
    return ((a-c)**2 + (b-d)**2)**0.5

time = collections.defaultdict(list)
n = int(input())

cannon = []
cannon.append((sx, sy))
for _ in range(n):
    x, y = map(float, input().split())
    cannon.append((x, y))
cannon.append((ex, ey))

for i in range(n+2):
    for j in range(n+2):
        if i == 0 or i == n+1:
            time[i].append((j, distance(cannon[i][0], cannon[i][1], cannon[j][0], cannon[j][1])/5))
        else:
            time[i].append((j, ((abs(distance(cannon[i][0], cannon[i][1], cannon[j][0], cannon[j][1])-50))/5)+2))

def dijkstra():
    ans = [1e9] * (n + 2)
    q = [(0, 0)]
    ans[0] = 0
    while q:
        d, node = heapq.heappop(q)
        if ans[node] < d:
            continue
        for v, w in time[node]:
            if d+w < ans[v]:
                ans[v] = d+w
                heapq.heappush(q, (d+w, v))
    print('%f'%(ans[-1]))
    return

dijkstra()