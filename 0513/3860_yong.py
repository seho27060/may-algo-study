import sys
input = sys.stdin.readline
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# 벨만토드의 기본을 잘 구현하면 풀 수 있는문제
# 난이도는 알고문제가 아니라 조건 때문에 플레인것 같음
def find():
    field[0][0] = 0
    for _ in range(W*H):
        for i in range(H):
            for j in range(W):
                if field[i][j] != 1000000000:
                    if time[i][j]:
                        for di, dj, t in time[i][j]:
                            if field[di][dj] > field[i][j] + t:
                                field[di][dj] = field[i][j] + t
                        # if di == H-1 and dj == W-1 and not flag:
                        #     ans
                        #     return
                        continue
                    if field[i][j] != 'X' and (i != H-1 or j != W-1):
                        for di, dj in d:
                            ni = i + di
                            nj = j + dj
                            if 0 <= ni < H and 0 <= nj < W and field[ni][nj] != 'X':
                                if field[ni][nj] > field[i][j] + 1:
                                    field[ni][nj] = field[i][j] + 1

    for i in range(H):
        for j in range(W):
            if field[i][j] != 1000000000:
                if time[i][j]:
                    for di, dj, t in time[i][j]:
                        if field[di][dj] > field[i][j] + t:
                            print('Never')
                            return
                    continue
                if field[i][j] != 'X' and (i != H-1 or j != W-1):
                    for di, dj in d:
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < H and 0 <= nj < W and field[ni][nj] != 'X':
                            if field[ni][nj] > field[i][j] + 1:
                                print('Never')
                                return
    if field[H-1][W-1] == 1000000000:
        print('Impossible')
        return
    print(field[H-1][W-1])

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    field = [[1000000000] * W for _ in range(H)]
    time = [[[] for _ in range(W)] for _ in range(H)]
    G = int(input())
    for _ in range(G):
        x, y = map(int, input().split())
        field[y][x] = 'X'
    E = int(input())
    for _ in range(E):
        x1, y1, x2, y2, t = map(int, input().split())
        time[y1][x1].append((y2, x2, t))
    find()