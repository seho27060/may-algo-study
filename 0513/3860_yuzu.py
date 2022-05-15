import sys
import collections
INF = sys.maxsize

def bf():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    time = [[INF] * (w) for _ in range(h)]
    time[0][0] = 0
    for i in range(n):
        c = 0
        for j in range(h):
            for k in range(w):
                if j == h-1 and k == w-1:
                    continue
                if time[j][k] == INF:
                    continue
                if graph[j][k] == 0:
                    for l in range(4):
                        nj = j+dx[l]
                        nk = k+dy[l]
                        if 0<=nj<h and 0<=nk<w and graph[nj][nk] != 1:
                            if time[nj][nk] > time[j][k]+1:
                                time[nj][nk] = time[j][k]+1
                                c = 1
                                if i == n - 1:
                                    return False
                elif graph[j][k] == 2:
                        njk, t = hole[(j, k)][0]
                        nj, nk = njk
                        if time[nj][nk] > time[j][k]+t:
                            time[nj][nk] = time[j][k]+t
                            c = 1
                            if i == n-1:
                                return False
        if c == 0:
            return time
    return time

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [[0] * (w) for _ in range(h)]
    n = w*h
    stonenum = int(input())
    for _ in range(stonenum):
        y, x = map(int, input().split())
        graph[x][y] = 1
    hole = collections.defaultdict(list)
    holenum = int(input())
    for _ in range(holenum):
        sy, sx, ey, ex, t = map(int, input().split())
        hole[(sx, sy)].append(((ex, ey), t))
        graph[sx][sy] = 2
    time = bf()
    if time:
        if time[-1][-1] != INF:
            print(time[-1][-1])
        else:
            print('Impossible')
    else:
        print('Never')