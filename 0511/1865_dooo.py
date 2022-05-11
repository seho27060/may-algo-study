def bf(start):
    d = [inf] * (n+1)
    d[start] = 0
    for i in range(n):
        for j in range(len(G)):
            now = G[j][0]
            next = G[j][1]
            dist = G[j][2]
            cost = dist+ d[now]
            if d[next] > cost:
                d[next] = cost
                if i == n-1:
                    return False
    return d
TC = int(input())
inf = 1e9
for _ in range(TC):
    n, m, w = map(int, input().split())
    G = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        G.append((a, b, c))
        G.append((b, a, c))
    for _ in range(w):
        a, b, c = map(int, input().split())
        G.append((a, b, -c))
    if not bf(1):
        print('YES')
    else:
        print('NO')