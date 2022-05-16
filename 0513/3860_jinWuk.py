import sys
from collections import defaultdict
def func():
    visited[0][0] = 0
    for i in range(W*H):
        for yy in range(H):
            for xx in range(W):
                if yy == H-1 and xx == W-1:
                    continue
                if visited[yy][xx] == TC:
                    continue
                if lst[yy][xx] == 0:
                    for u in range(4):
                        Y = yy + dy[u]
                        X = xx + dx[u]

                        if Y < 0 or Y >= H or X < 0 or X >= W or lst[Y][X] == 1:
                            continue
                        if visited[Y][X] > visited[yy][xx] + 1:
                            visited[Y][X] = visited[yy][xx] + 1
                            if i == W*H - 1:
                                return True

                elif lst[yy][xx] == 2:
                    YY, XX, t = hole[(yy, xx)][0]
                    if visited[YY][XX] > visited[yy][xx] + t:
                        visited[YY][XX] = visited[yy][xx] + t
                        if i == W*H - 1:
                            return True
    return False



dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

TC = sys.maxsize
for _ in range(TC):
    W,H = map(int,input().split())
    if W ==0 and H ==0:
        break
    lst = [[0]*W for _ in range(H)]
    G= int(input())
    for _ in range(G):
        x,y = map(int,input().split())
        lst[y][x] = 1
    E =int(input())
    hole = defaultdict(list)
    for _ in range(E):
        x1,y1,x2,y2,T = map(int,input().split())
        lst[y1][x1] = 2
        hole[(y1,x1)].append((y2,x2,T))
    visited = [[TC] * W for _ in range(H)]
    result = func()
    if result:
        print('Never')
    else:
        if visited[H-1][W-1] == TC:
            print('Impossible')
        else:
            print(visited[H-1][W-1])