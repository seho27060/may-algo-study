import sys
input = sys.stdin.readline
from heapq import heappush, heappop


def calDist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def f():
    qu = []
    heappush(qu, (0, 0))
    time[0] = 0
    while qu:
        curT, curN = heappop(qu)

        if time[curN] < curT:
            continue

        for newN, newT in G[curN]:
            if time[newN] > curT + newT:
                time[newN] = curT + newT
                heappush(qu, (curT + newT, newN))

Sx, Sy = map(float, input().split())
Ex, Ey = map(float, input().split())

N = int(input())
cannon = []
cannon.append([Sx, Sy])
G = [[] for _ in range(N + 2)]
for i in range(1, N + 1):
    Cx, Cy = map(float, input().split())
    cannon.append([Cx, Cy])
    # 시작부터 대포까지 걸어가면
    dist = calDist(cannon[0], cannon[i])
    t = dist / 5
    G[0].append([i, t])
cannon.append([Ex, Ey])

# 시작부터 끝점까지 걸어가면
dist = calDist(cannon[0], cannon[N + 1])
t = dist / 5
G[0].append([N + 1, t])

# 각 대포마다 순회
for i in range(1, N + 1):
    # 끝점포함 시간 계산
    for k in range(1, N + 2):
        if i == k:
            continue
        # 걸어가면
        dist = calDist(cannon[i], cannon[k])
        # 하지만 대포
        dist = abs(dist - 50)
        t = dist / 5 + 2
        G[i].append([k, t])
INF = 999999999999999
time = [INF] * (N + 2)
f()
# print(time)
print(time[N + 1])
