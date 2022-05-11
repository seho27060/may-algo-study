from collections import defaultdict
import sys
input = sys.stdin.readline
INF = sys.maxsize

def BF():
    D = [INF] * (N + 1)
    D[1] = 0
    for i in range(N):
        for n1 in range(1, N+1):
            if n1 == INF:
                continue
            for t, n2 in G[n1]:
                if D[n2] > t + D[n1]:
                    D[n2] = t + D[n1]
                    if i == (N-1):
                        return True
    return False

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    G = defaultdict(list)
    for _ in range(M):
        S, E, T = map(int, input().split())
        G[S].append((T, E))
        G[E].append((T, S))
    for _ in range(W):
        S, E, T = map(int, input().split())
        G[S].append((-T, E))

    if BF():
        print('YES')
    else:
        print('NO')

# 시작점이 어디든 음수 사이클만 존재하는 것을 확인하면 YES...