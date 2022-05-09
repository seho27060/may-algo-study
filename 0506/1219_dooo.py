def bfs(start):
    q = []
    q.append(start)
    v = [0] * n
    while q:
        c = q.pop(0)
        if c == e:
            return True
        for i in range(m):
            bn = G[i][0]
            bx = G[i][1]
            if c == bn and v[bx] == 0:
                q.append(bx)
                v[bx]= 1

    return False

def bf(start):
    global flag
    d[start] = lst[start]
    for i in range(n):

        for j in range(m):
            now = G[j][0]
            next = G[j][1]
            dist = G[j][2]
            cost = lst[next] - dist + d[now]
            if d[now] != inf and d[next] < cost:
                d[next] = cost

                if i == n-1:
                    if bfs(now):
                        return True

    return False



n, s, e, m= map(int, input().split())
inf = -1e9
G = []
d = [inf] * (n)
flag = True
for i in range(m):
    a, b, c = map(int, input().split())
    G.append((a, b, c))
lst = list(map(int, input().split()))
if bf(s):
    print('Gee')
elif d[e] == inf:
    print('gg')
else:
    print(d[e])