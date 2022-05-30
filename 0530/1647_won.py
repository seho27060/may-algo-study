import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = []
for _ in range(M):
    A, B, C = map(int, input().split())
    G.append([A, B, C])
G.sort(key=lambda x: x[2])

parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

ans = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

arr = []
for A, B, C in G:
    if find(A) != find(B):
        union(A, B)
        ans += C
        arr.append(C)

ans -= arr[-1]
print(ans)
