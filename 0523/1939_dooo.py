def bfs(s, e, w):
    q = []
    q.append(s)
    v = [0] * (n+1)
    v[s] = 1
    while q:
        c = q.pop(0)
        if c == e:
            return v[c]
        for lst in G[c]:

            next, weight = lst
            if v[next] == 0 and weight >= w:
                q.append((next))
                v[next] = 1

    return False
n, m = map(int, input().split())
G = [[] for _ in range(n+1)]
start = 1e9
end = -1
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))
    if start > c:
        start = c
    if end < c:
        end = c

s, e = map(int, input().split())

while start <= end:
    mid = (start+end) //2
    if bfs(s, e, mid):
        start = mid + 1
    else:
        end = mid - 1

print(start-1)