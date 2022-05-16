from collections import defaultdict
import sys
input = sys.stdin.readline

def bf():
    for j in range(W*H):
        for nowy in range(H):
            for nowx in range(W):
                cnt = result[nowy][nowx]
                if (nowx == W-1 and nowy ==0) or cnt == 99999999999 or road[nowy][nowx] == 2:
                    continue
                elif road[nowy][nowx] == 3:                     #원래 딕셔너리에서 검색하도록했는데 시간초과뜨고
                    eX = Edict[(nowx, nowy)][0]                 # road라는 각위치 특성 따로 표시해둘 지도 만들었더니 통과..
                    eY = Edict[(nowx, nowy)][1]
                    ecnt = Edict[(nowx, nowy)][2]
                    if result[eY][eX] > cnt + ecnt:
                        result[eY][eX] = cnt + ecnt
                        if j == W*H-1:
                            return True
                else:
                    for i in range(4):
                        X = nowx + dx[i]
                        Y = nowy + dy[i]
                        
                        if 0<=X<W and 0<=Y<H and road[Y][X] != 2:
                            if result[Y][X] > cnt+1:
                                result[Y][X] = cnt+1
                                if j == W*H-1:
                                    return True
    return False


while 1:
    W,H = map(int,input().split())
    if W==0 and H ==0:
        break

    road = [[1]*W for _ in range(H)]

    G = int(input())
    Glist =[]
    for _ in range(G):
        gx,gy=map(int, input().split())
        road[H-1-gy][gx] = 2

    E = int(input())
    Edict=defaultdict(list)
    for _ in range(E):
        x1,y1,x2,y2,t = map(int,input().split())
        road[H-1-y1][x1] = 3
        Edict[x1,H-1-y1] = [x2,H-1-y2,t]

    result=[[99999999999]*W for _ in range(H)]
    result[H-1][0] = 0

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    if bf():
        print('Never')
    else:
        if result[0][W-1] == 99999999999:
            print('Impossible')
        else:
            print(result[0][W-1])
