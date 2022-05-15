import sys
input = sys.stdin.readline
from collections import deque
import collections


dr = (1, -1, 0, 0)
dc = (0, 0, -1, 1)

def f():
    time[0][0] = 0
    for i in range(W * H):
        for r in range(H):
            for c in range(W):
                if r == H - 1 and c == W - 1:
                    continue
                if time[r][c] == INF:
                    continue
                if MAP[r][c] == 0:
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]

                        if nr < 0 or nr >= H or nc < 0 or nc >= W or MAP[nr][nc] == 1:
                            continue
                        if time[nr][nc] > time[r][c] + 1:
                            time[nr][nc] = time[r][c] + 1
                            if i == W * H - 1:
                                return True

                elif MAP[r][c] == 2:
                    nr, nc, t = holes[(r, c)][0]
                    if time[nr][nc] > time[r][c] + t:
                        time[nr][nc] = time[r][c] + t
                        if i == W * H - 1:
                            return True
    return False

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    # 전체 지도
    MAP = [[0] * W for _ in range(H)]
    G = int(input())
    for _ in range(G):
        X, Y = map(int, input().split())
        # 묘비를 1로 표시
        MAP[Y][X] = 1
    E = int(input())
    holes = collections.defaultdict(list)
    for _ in range(E):
        X1, Y1, X2, Y2, T = map(int, input().split())
        # 귀신 구멍은 2로 표시
        MAP[Y1][X1] = 2
        holes[(Y1, X1)].append((Y2, X2, T))
    INF = 100000001
    time = [[INF] * W for _ in range(H)]
    result = f()
    if result:
        print('Never')
    else:
        ans = time[H - 1][W - 1]
        if ans == INF:
            print('Impossible')
        else:
            print(ans)
    # print(time)