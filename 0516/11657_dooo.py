def bf(start):
    d[start] = 0
    for i in range(n):
        for j in range(m):
            now = G[j][0]
            next = G[j][1]
            dist = G[j][2]
            if d[now] != inf and d[next] > d[now] + dist:
                d[next] = d[now]+ dist
                if i == n-1:
                    return False
    return True

n, m = map(int, input().split())
G = []
for _ in range(m):
    a, b, c = map(int, input().split())
    G.append((a,b,c))

inf = 1e9
d = [inf] * (n+1)
sol = bf(1)
if not sol:
    print(-1)
else:
    for j in range(2,n+1):
        if d[j] == inf:
            print(-1)
        else:
            print(d[j])