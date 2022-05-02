import sys
from collections import deque

def func():
    visited = [[T]*N for _ in range(N)]
    q = deque()
    q.append([0,0])
    visited[0][0]= lst[0][0]
    while q:
        y,x = q.popleft()
        for j in range(4):
            Y = y+dy[j]
            X = x+dx[j]
            if 0<= Y <N and 0<= X <N:
                cnt = visited[y][x] + lst[Y][X]
                if visited[Y][X] > cnt:
                    visited[Y][X] = cnt
                    q.append([Y,X])
    return visited[N-1][N-1]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

T = sys.maxsize
for i in range(T):
    N = int(input())
    if N == 0:
        break
    lst = [list(map(int,input().split())) for _ in range(N)]
    print(f'Problem {i+1}:', func())

