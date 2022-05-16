import sys
input = sys.stdin.readline


def f():
    time[1] = 0

    for i in range(N):
        for curN in range(1, N + 1):
            for newN, t in G[curN]:
                if time[curN] == INF:
                    continue
                if time[newN] > time[curN] + t:
                    time[newN] = time[curN] + t
                    if i == N - 1:
                        return True
    return False


N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((B, C))

INF = 5000001
time = [INF] * (N + 1)
result = f()

if result:
    print(-1)
else:
    for i in range(2, N + 1):
        if time[i] == INF:
            print(-1)
        else:
            print(time[i])
