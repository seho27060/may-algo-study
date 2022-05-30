def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(p, a, b):
    a = find(p, a)
    b = find(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


n, m = map(int, input().split())
p = [0] * (n+1)
G = []
for i in range(1, n+1):
    p[i] = i
total = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    total += c
    G.append((c, a, b))
G.sort()
val = 0
last = 0
for e in G:
    cost, now, next = e

    if find(p, now) != find(p, next):
        union(p, now, next)
        val += cost
        last = cost
print(val-last)
