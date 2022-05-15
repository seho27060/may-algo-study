### 220515 3860 할로윈 묘지
## 0,0 -> w-1, h-1 으로
## 시간==가중치(음수의 가중치가 포함된 노드)
## 이동은 동서남북
## 묘비는 벽, 구멍은 워프, 잔디는 이동가능
## 음수사이클이라면 Never/ 출구로갈수없다면 impossible/ 그외의 경우 걸리는 가장빠른 시간.
##
import sys
from collections import defaultdict

INF = sys.maxsize
input = sys.stdin.readline

## 노드*간선
def bf():
    global w, h, graves, warp
    moves = [[0,1],[0,-1],[1,0],[-1,0]]
    visited = [[INF]*w for _ in range(h)]

    visited[0][0] = 0

    for i in range(w*h-1):
        for H in range(h):
            for W in range(w):
                if H == h-1 and W == w-1:
                    continue
                if visited[H][W] == INF:
                    continue

                if graves[H][W] == 0:
                    for move in moves:
                        nxtW, nxtH = W + move[0], H + move[1]
                        if 0 <= nxtW < w and 0 <= nxtH < h:
                            if visited[H][W] + 1 < visited[nxtH][nxtW]:
                                visited[nxtH][nxtW] = visited[H][W] + 1
                elif graves[H][W] == 2:
                    for nxtH, nxtW, nxtCost in warp[(H, W)]:
                        # print(H,W, warp[(H,W)], visited[H][W] + nxtCost,visited[nxtH][nxtW])
                        if visited[nxtH][nxtW] > visited[H][W] + nxtCost:
                            visited[nxtH][nxtW] = visited[H][W] + nxtCost

    cycle = False

    for H in range(h):
        for W in range(w):
            if H == h - 1 and W == w - 1:
                continue
            if visited[H][W] == INF:
                continue
            if graves[H][W] == 0:
                for move in moves:
                    nxtW, nxtH = W + move[0], H + move[1]
                    if 0 <= nxtW < w and 0 <= nxtH < h:
                        if graves[nxtH][nxtW] == 0:
                            if visited[H][W] + 1 < visited[nxtH][nxtW]:
                                cycle = True
                                break
            elif graves[H][W] == 2:
                for nxtH, nxtW, nxtCost in warp[(H,W)]:
                    if visited[nxtH][nxtW] > visited[H][W] + nxtCost:
                        cycle = True
                        break
            if cycle:
                break
        if cycle:
            break

    # for H in range(h):
    #     print(visited[H])
    # print()
    if cycle:
        return "Never"
    else:
        if visited[h-1][w-1] < INF:
            return visited[h-1][w-1]
        else:
            return "Impossible"


while 1:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    g = int(input()) # 묘비갯수미정 ㅋㅋ
    graves = [[0]*w for _ in range(h)]
    for _ in range(g):
        x,y = map(int,input().split())
        graves[y][x] = 1
    e = int(input()) # 귀신구멍
    warp = defaultdict(list)
    for _ in range(e):
        x1, y1, x2, y2, t = map(int,input().split())
        graves[y1][x1] = 2
        warp[(y1,x1)].append((y2,x2,t))

    # print("grave")
    # for H in range(h):
    #     print(graves[H])
    # print()
    answer = bf()
    print(answer)