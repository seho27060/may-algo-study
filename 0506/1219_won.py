import sys
input = sys.stdin.readline
from collections import deque

def check(S):
    visited = [0] * N
    qu = deque()
    qu.append(S)
    while qu:
        t = qu.popleft()

        if t == E:
            return True

        for v, _ in G[t]:
            if visited[v] == 0:
                qu.append(v)
                visited[v] = 1
    return False

def f():
    for i in range(N + 1):
        if i == N and moneyArr[E] == -INF:
            print('gg')
            return False
        for k in range(N):
            if moneyArr[k] == -INF:
                continue
            for node, money in G[k]:
                if moneyArr[node] < moneyArr[k] + money:
                    moneyArr[node] = moneyArr[k] + money
                    if i == N and check(node):
                        print('Gee')
                        return False
    return True

INF = float('inf')
N, S, E, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    G[u].append([v, w])

reward = list(map(int, input().split()))
moneyArr = [-INF] * N

moneyArr[S] = reward[S]
for i in range(N):
    for k in range(len(G[i])):
        for p in range(N):
            if G[i][k][0] == p:
                G[i][k][1] = reward[p] - G[i][k][1]

if f():
    print(moneyArr[E])
