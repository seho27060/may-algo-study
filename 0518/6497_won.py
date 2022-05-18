import sys
input = sys.stdin.readline


def find_parent(a, parent):
    if parent[a] != a:
        parent[a] = find_parent(parent[a], parent)
    return parent[a]

def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    edges = []
    parent = [i for i in range(m + 1)]
    for _ in range(m):
        x, y, z = map(int, input().split())
        edges.append((x, y, z))

    edges.sort(key=lambda x: x[2])
    ans = 0
    for edge in edges:
        x, y, z = edge
        if find_parent(x, parent) == find_parent(y, parent):
            ans += z
        else:
            union_parent(x, y, parent)
    print(ans)
