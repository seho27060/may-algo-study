import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
    edges.append((w, v, u))
edges.sort(reverse=True)

s, e = map(int, input().split())

ans = 0
for edge in edges:
    cost, a, b = edge
    if find(s) != find(e):
        union(a, b)
        ans = cost
print(ans)