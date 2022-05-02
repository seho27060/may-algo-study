t=0
while 1:
    t += 1
    N = int(input())
    if N == 0: break
    Nlist=[]
    for _ in range(N):
        Nlist.append(list(map(int,input().split())))

    result=[[N*N*9+1]*N for _ in range(N)]
    result[0][0] = Nlist[0][0]

    ST=[[0,0,Nlist[0][0]]]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while ST:
        x,y,cnt =ST.pop(0)

        if cnt > result[y][x]:
            continue

        for i in range(4):
            X= x + dx[i]
            Y= y + dy[i]
            if 0<=X<N and 0<=Y<N and result[Y][X] > cnt+Nlist[Y][X]:
                result[Y][X] = cnt+Nlist[Y][X]
                ST.append([X,Y,cnt+Nlist[Y][X]])

    print('Problem {}: {}'.format(t,result[N-1][N-1]))
