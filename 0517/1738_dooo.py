def bf(start):
    d[start] = 0

    for i in range(n):
        for j in range(m):
            now = G[j][0]
            next = G[j][1]
            dist = G[j][2]
            cost = d[now] + dist
            if d[now] != inf and d[next] < cost:
                d[next] = cost
                v[next] = now
                if i == n-1 and next == n:
                    return False
                elif i == n-1:
                    for k in G:
                        if k[0] == next and k[1] == n:
                            return False

    return True

n, m = map(int, input().split())
G = []
for _ in range(m):
    a, b, c = map(int, input().split())
    G.append((a, b, c))
inf = 1234567890987654321
d = [-inf] * (n+1)
v = [0] * (n+1)
if bf(1):
    lst = [n]
    k = n
    while k >1:
        if v[k] != 0:
            lst.append(v[k])
            k = v[k]
        else:
            k -= 1
    for i in range(len(lst)-1,-1,-1):
        print(lst[i], end = ' ')
else:
    print(-1)
