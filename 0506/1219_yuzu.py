import sys
import collections
INF = sys.maxsize

n, s, e, m = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def check(x):
    visited = [0]*(n)
    q = [(x)]
    while q:
        x = q.pop(0)
        if x == e:
            return True
        for v, w in graph[x]:
            if visited[v] == 0:
                q.append(v)
                visited[v] = 1

money = list(map(int, input().split()))
dist = [-INF] * (n)
dist[s] = money[s]
def bf(s):
    for i in range(n):
        for j in range(m):
            for v, w in graph[j]:
                if dist[j] != -INF and dist[v] < dist[j] - w + money[v]:
                    dist[v] = dist[j] - w + money[v]
                    if i==(n-1):
                        if check(v):
                            return True
    return False

if bf(s):
    print('Gee')
else:
    if dist[e] == -INF:
        print('gg')
    else:
        print(dist[e])