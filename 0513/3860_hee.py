import sys
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize

def BF(W, H):
    D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    Dijk[0][0] = 0
    for i in range(W * H):
        for x in range(W):
            for y in range(H):
                if (Dijk[y][x] == INF) or (x == W-1 and y == H-1) or not MAP[y][x]:
                    continue
                if MAP[y][x] == 1:
                    for d in D:
                        nx = x + d[0]
                        ny = y + d[1]
                        if -1 < nx < W and -1 < ny < H:
                            if Dijk[y][x] + 1 < Dijk[ny][nx]:
                                Dijk[ny][nx] = Dijk[y][x] + 1
                                if i == W * H - 1:
                                    return True
                else:
                    nx, ny, T = ghost[(x, y)][0]
                    if Dijk[y][x] + T < Dijk[ny][nx]:
                        Dijk[ny][nx] = Dijk[y][x] + T
                        if i == W * H - 1:
                            return True

    return False

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break

    MAP = [[1] * W for _ in range(H)]

    G = int(input())
    for _ in range(G):
        X, Y = map(int, input().split())
        MAP[Y][X] = 0

    ghost = defaultdict(list)
    E = int(input())
    for _ in range(E):
        X1, Y1, X2, Y2, T = map(int, input().split())
        ghost[(X1, Y1)].append((X2, Y2, T))
        MAP[Y1][X1] = -1

    Dijk = [[INF] * W for _ in range(H)]

    if BF(W, H):
        print("Never")
    elif Dijk[-1][-1] == INF:
        print("Impossible")
    else:
        print(Dijk[-1][-1])