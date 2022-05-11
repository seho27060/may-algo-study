import sys
input = sys.stdin.readline


T = int(input())

def f(s):
    time[s] = 0
    for i in range(N):
        for curN, newN, cost in G:

            if time[newN] > time[curN] + cost:
                time[newN] = time[curN] + cost

                if i == N - 1:
                    return True
    return False

for _ in range(T):
    N, M, W = map(int, input().split())
    G = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        G.append([S, E, T])
        G.append([E, S, T])
    for _ in range(W):
        S, E, T = map(int, input().split())
        G.append([S, E, -T])
    INF = 99999999999999999999
    time = [INF] * (N + 1)
    result = f(1)
    if result:
        print('YES')
    else:
        print('NO')

