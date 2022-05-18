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

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    parent = [i for i in range(m)]
    visited = [0]*m
    edges = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))
    edges.sort()

    ans = 0
    for edge in edges:
        dist, a, b = edge
        if find(a) != find(b):
            union(a, b)
        else:
            ans += dist
    print(ans)