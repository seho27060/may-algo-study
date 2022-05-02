import heapq


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

inf = 1e9
tc = 1
def dijk(sx, sy):
    q = []
    d[sx][sy] = arr[sx][sy]
    heapq.heappush(q, (d[sx][sy], sx, sy))
    while q:
        dist, cx, cy = heapq.heappop(q)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = d[cx][cy] + arr[nx][ny]
                if cost < d[nx][ny]:
                    d[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

while True:
    n = int(input())
    if n == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]
    d = [[inf] * n for _ in range(n)]
    dijk(0, 0)
    print('Problem {}: {}'.format(tc, d[n-1][n-1]))
    tc += 1