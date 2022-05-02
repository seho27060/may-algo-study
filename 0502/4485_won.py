import sys
input = sys.stdin.readline
from heapq import heappush, heappop


dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
INF = 140626
tc = 0
while True:
    N = int(input())
    if N == 0:
        break
    else:
        tc += 1
        G = [list(map(int, input().split())) for _ in range(N)]
        distArr = [[INF] * N for _ in range(N)]

        qu = []
        qu.append((G[0][0], 0, 0))
        distArr[0][0] = 0
        while qu:
            dist, r, c = heappop(qu)

            if r == N - 1 and c == N - 1:
                ans = distArr[r][c]
                break

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < N and distArr[nr][nc] > dist + G[nr][nc]:
                    distArr[nr][nc] = dist + G[nr][nc]
                    heappush(qu, (dist + G[nr][nc], nr, nc))

        print("Problem {}: {}".format(tc, ans))
