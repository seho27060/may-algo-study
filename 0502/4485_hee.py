from heapq import *
import sys
INF = sys.maxsize
input = sys.stdin.readline
D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = 0

while True:
    T += 1
    N = int(input())
    if N == 0:
        break

    G = []
    for _ in range(N):
        G.append(list(map(int, input().split())))

    Q = [(G[0][0], 0, 0)]
    DK = [[INF] * N for _ in range(N)]
    DK[0][0] = G[0][0]

    while Q:
        k, x, y = heappop(Q)
        for d in D:
            nx = x + d[0]
            ny = y + d[1]
            if -1 < nx < N and -1 < ny < N and k + G[ny][nx] < DK[ny][nx]:
                DK[ny][nx] = k + G[ny][nx]
                heappush(Q, (DK[ny][nx], nx, ny))

    print('Problem %d: %d'%(T, DK[-1][-1]))