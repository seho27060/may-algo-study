
import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def dijkstra():
    Q = [(MAP[0][0], 0, 0)]
    D = [[1e10] * N for _ in range(N)]
    D[0][0] = MAP[0][0]

    while Q:
        rupee, curR, curC = heappop(Q)
        if curR == curC == N - 1: return rupee

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < N and 0 <= newC < N:
                if D[newR][newC] > rupee + MAP[newR][newC]:
                    heappush(Q, (rupee + MAP[newR][newC], newR, newC))
                    D[newR][newC] = rupee + MAP[newR][newC]


t = 0
while True:
    N = int(input())
    if N == 0: break
    MAP = [list(map(int, input().split())) for _ in range(N)]
    t += 1
    print(f'Problem {t}: {dijkstra()}')