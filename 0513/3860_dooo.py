dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bf():
    d[0][0] = 0

    for k in range(cnt):
        for i in range(n):
            for j in range(m):
                if d[i][j] == inf or (i == n-1 and j == m-1):
                    continue
                if arr[i][j] == 1:
                    continue
                if arr[i][j] == 0:

                    for mv in range(4):
                        nx = i + dx[mv]
                        ny = j + dy[mv]
                        if 0 <= nx <n and 0 <= ny < m:

                            if d[nx][ny] > d[i][j] + 1:
                                d[nx][ny] = d[i][j] + 1
                                if k == cnt-1:
                                    return False
                elif arr[i][j] == 2:

                    nx, ny, dist = G[i][j][0]
                    if d[nx][ny] > d[i][j] + dist:
                        d[nx][ny] = d[i][j] + dist
                        if k == cnt-1:
                            return False
    return True

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    arr = [[0] * m for _ in range(n)]
    G = [[[] for _ in range(m)] for _ in range(n)]
    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1
    t = int(input())
    for _ in range(t):
        a, b, c, d, e = map(int, input().split())
        arr[b][a] = 2
        G[b][a].append((d, c, e))

    cnt = n*m


    inf = 12345678987654321
    d = [[inf] * m for _ in range(n)]
    sol = bf()
    if sol == True:
        if d[n-1][m-1] == inf:
            print('Impossible')
        else:
            print(d[n-1][m-1])

    else:
        print('Never')